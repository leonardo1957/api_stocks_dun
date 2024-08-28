from django.db import models

class Competitor(models.Model):
    name = models.CharField(max_length=255)
    market_cap_currency = models.CharField(max_length=10)
    market_cap_value = models.FloatField()

class Stock(models.Model):
    status = models.CharField(max_length=255)
    purchased_amount = models.IntegerField(default=0)
    purchased_status = models.CharField(max_length=255)
    request_data = models.DateField()
    company_code = models.CharField(max_length=10)
    company_name = models.CharField(max_length=255)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    five_days = models.FloatField()
    one_month = models.FloatField()
    three_months = models.FloatField()
    year_to_date = models.FloatField()
    one_year = models.FloatField()
    competitors = models.ManyToManyField(Competitor)
