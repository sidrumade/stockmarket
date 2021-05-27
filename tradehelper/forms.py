from django import forms


class TradeCalculatorForm(forms.Form):
    My_Portfolio = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'my_portfolio',
            'aria-describedby': 'my_portfolioHelp'
        }
    ))
    High_of_Green_Candle = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'high_of_green_candle',
            'aria-describedby': 'high_of_green_candleHelp'
        }
    ))
    Lowest_Low = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'lowest_low',
            'aria-describedby': 'lowest_lowHelp'
        }
    ))
    Risk = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'risk',
            'aria-describedby': 'riskHelp'
        }
    ))
    Required_Portfolio = forms.FloatField(required=False, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'required_portfolio',
            'aria-describedby': 'required_portfolioHelp'
        }
    ))
    Entry = forms.FloatField(required=False, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'entry',
            'aria-describedby': 'entryHelp'
        }
    ))
    StopLoss = forms.FloatField(required=False, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'stoploss',
            'aria-describedby': 'stoplossHelp'
        }
    ))
    Difference = forms.FloatField(required=False, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'difference',
            'aria-describedby': 'differenceHelp'
        }
    ))
    Quantity = forms.FloatField(required=False, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'quantity',
            'aria-describedby': 'quantityHelp'
        }
    ))
    Target_1 = forms.FloatField(required=False, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'target1',
            'aria-describedby': 'target1Help'
        }
    ))
    Target_2 = forms.FloatField(required=False, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'target2',
            'aria-describedby': 'target2Help'
        }
    ))
    Target_3 = forms.FloatField(required=False, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'target3',
            'aria-describedby': 'target3Help'
        }
    ))
