from django import forms
from .models import StockRecords
from django.utils import timezone


class StockRecordsForm(forms.ModelForm):
    #buy_date = forms.DateField(initial=timezone.now)

    class Meta:
        model = StockRecords
        fields = '__all__'
        widgets = {
            'user': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'portfolio': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.widgets.Select(attrs={'class': 'form-control'}),
            'stock_type': forms.widgets.Select(attrs={'class': 'form-control'}),
            'buy_date': forms.widgets.DateInput(attrs={'class': 'form-control'}),
            'entry': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'stoploss': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'target': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'exit': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'profit_loss_per_stock': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'profile': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'emotion': forms.widgets.Select(attrs={'class': 'form-control'}),
            'mistake': forms.widgets.Select(attrs={'class': 'form-control'}),
            'graph': forms.widgets.FileInput(attrs={'class': 'form-control-file'}),

        }

