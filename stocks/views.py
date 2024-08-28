from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Competitor, Stock
from .serializers import StockSerializer
from .services import get_polygon_stock_data
from .scraping import scrape_marketwatch
from django.core.cache import cache
from datetime import datetime

@api_view(['GET'])
def get_stock(request, stock_symbol):
    cache_key = f'stock_data_{stock_symbol}'
    cached_data = cache.get(cache_key)

    if cached_data:
        return Response(cached_data)

    today_date = datetime.now().strftime('%Y-%m-%d')
    polygon_data = get_polygon_stock_data(stock_symbol, today_date)

    if polygon_data['status'] == 'success':
        performance_data, competitors_data = scrape_marketwatch(stock_symbol)

        stock, created = Stock.objects.get_or_create(
            company_code=stock_symbol,
            defaults={
                'status': 'active',
                'purchased_amount': 0,
                'purchased_status': 'not purchased',
                'request_data': today_date,
                'company_name': stock_symbol.upper(),
                'open': polygon_data['open'],
                'high': polygon_data['high'],
                'low': polygon_data['low'],
                'close': polygon_data['close'],
                'five_days': performance_data.get('five_days'),
                'one_month': performance_data.get('one_month'),
                'three_months': performance_data.get('three_months'),
                'year_to_date': performance_data.get('year_to_date'),
                'one_year': performance_data.get('one_year'),
            }
        )


        for competitor_data in competitors_data:
            competitor, _ = Competitor.objects.get_or_create(**competitor_data)
            stock.competitors.add(competitor)

        serializer = StockSerializer(stock)
        cache.set(cache_key, serializer.data, timeout=60*15)
        return Response(serializer.data)

    return Response(polygon_data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_stock(request, stock_symbol):
    try:
        stock = Stock.objects.get(company_code=stock_symbol)
        amount = request.data.get("amount")
        stock.purchased_amount += amount
        stock.save()
        return Response({"message": f"{amount} units of stock {stock_symbol} were added to your stock record"}, status=status.HTTP_201_CREATED)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
