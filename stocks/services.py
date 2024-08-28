import requests
from django.conf import settings

def get_polygon_stock_data(stock_symbol, date):
    url = f"https://api.polygon.io/v1/open-close/{stock_symbol}/{date}"
    headers = {
        'Authorization': f'Bearer {settings.POLYGON_API_KEY}'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return {
            'status': 'success',
            'open': data['open'],
            'high': data['high'],
            'low': data['low'],
            'close': data['close']
        }
    else:
        return {
            'status': 'error',
            'message': 'Could not retrieve data from Polygon.io'
        }
