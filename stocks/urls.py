from django.urls import path
from .views import get_stock, update_stock

urlpatterns = [
    path('stock/<str:stock_symbol>/', get_stock, name='get_stock'),
    path('stock/<str:stock_symbol>/', update_stock, name='update_stock'),
]
