from django.urls import path, re_path
from .views import TradeCalculatorFormView

app_name = 'tradehelper'

urlpatterns = [
    path('', TradeCalculatorFormView.as_view(), name='tradecalculatorform'),
]
