from django.db import models

class Stock(models.Model):
    company_code = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=20)
    purchased_amount = models.DecimalField(max_digits=12, decimal_places=2)
    purchased_status = models.CharField(max_length=20)
    request_data = models.DateField()
    company_name = models.CharField(max_length=100)
    open = models.DecimalField(max_digits=12, decimal_places=2)
    high = models.DecimalField(max_digits=12, decimal_places=2)
    low = models.DecimalField(max_digits=12, decimal_places=2)
    close = models.DecimalField(max_digits=12, decimal_places=2)
    five_days = models.FloatField(null=True, blank=True)
    one_month = models.FloatField(null=True, blank=True)
    three_months = models.FloatField(null=True, blank=True)
    year_to_date = models.FloatField(null=True, blank=True)
    one_year = models.FloatField(null=True, blank=True)
    competitors = models.ManyToManyField('Competitor', related_name='stocks', blank=True)

    def __str__(self):
        return self.company_name

class Competitor(models.Model):
    name = models.CharField(max_length=100)
    market_cap_currency = models.CharField(max_length=10)
    market_cap_value = models.DecimalField(max_digits=20, decimal_places=2)
    stock = models.ForeignKey(Stock, related_name='competitor_set', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
