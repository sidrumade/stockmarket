from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import TradeCalculatorForm


# Create your views here.

class TradeCalculatorFormView(FormView):
    form_class = TradeCalculatorForm
    template_name = 'tradehelper/TradeCalculator.html'

    def get(self, request, *args, **kwargs):
        my_portfolio = request.GET.get('My_Portfolio')
        high_of_green_candle = request.GET.get('High_of_Green_Candle')
        lowest_low = request.GET.get('Lowest_Low')
        risk = request.GET.get('Risk')

        context = {
            'form': self.get_form(),
            'My_Portfolio': my_portfolio,
            'High_of_Green_Candle': high_of_green_candle,
            'Lowest_Low': lowest_low,
            'Risk': risk
        }
        return render(request, 'tradehelper/TradeCalculator.html', context)
