from rest_framework import serializers
from .models import Stock, Competitor

class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitor
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    competitors = CompetitorSerializer(many=True)

    class Meta:
        model = Stock
        fields = '__all__'
