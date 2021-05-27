import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class StockRecords(models.Model):
    NIFTY_BETA_STOCKS = [('AXIS Bank', 'AXIS Bank'),
                         ('Adani Enterprises', 'Adani Enterprises'),
                         ('Adani Port & SEZ', 'Adani Port & SEZ'),
                         ('Adani Power', 'Adani Power'),
                         ('Ashok Leyland', 'Ashok Leyland'),
                         ('Bank Of Baroda', 'Bank Of Baroda'),
                         ('Bank of India', 'Bank of India'),
                         ('CG Power and Industrial Solutions', 'CG Power and Industrial Solutions'),
                         ('Canara Bank', 'Canara Bank'),
                         ('Century Textiles', 'Century Textiles'),
                         ('DLF', 'DLF'),
                         ('Dewan Housing', 'Dewan Housing'),
                         ('GMR Infrastructure', 'GMR Infrastructure'),
                         ('Hindalco Industries', 'Hindalco Industries'),
                         ('Housing Development', 'Housing Development'),
                         ('ICICI Bank', 'ICICI Bank'),
                         ('IDBI Bank', 'IDBI Bank'),
                         ('IFCI', 'IFCI'),
                         ('IRB Infrastructure', 'IRB Infrastructure'),
                         ('India Cements', 'India Cements'),
                         ('Indiabulls RE', 'Indiabulls RE'),
                         ('JSW Energy', 'JSW Energy'),
                         ('Jain Irrigation', 'Jain Irrigation'),
                         ('Jindal Steel&Power', 'Jindal Steel&Power'),
                         ('Jubilant Pharmova', 'Jubilant Pharmova'),
                         ('Karnataka Bank', 'Karnataka Bank'),
                         ('Larsen & Toubro', 'Larsen & Toubro'),
                         ('Lic Housing Finance', 'Lic Housing Finance'),
                         ('Motherson Sumi Systems', 'Motherson Sumi Systems'),
                         ('NCC', 'NCC'),
                         ('PTC India', 'PTC India'),
                         ('Power Finance', 'Power Finance'),
                         ('Punjab National Bank', 'Punjab National Bank'),
                         ('REC', 'REC'),
                         ('Reliance Capital', 'Reliance Capital'),
                         ('Reliance Communications', 'Reliance Communications'),
                         ('Reliance Infrastructure', 'Reliance Infrastructure'),
                         ('Reliance Power', 'Reliance Power'),
                         ('SBI', 'SBI'),
                         ('Suzlon Energy', 'Suzlon Energy'),
                         ('TV18 Broadcast', 'TV18 Broadcast'),
                         ('Tata Elxsi', 'Tata Elxsi'),
                         ('Tata Motors', 'Tata Motors'),
                         ('Tata Steel Ltd', 'Tata Steel Ltd'),
                         ('Union Bank of India', 'Union Bank of India'),
                         ('Vedanta', 'Vedanta'),
                         ('Voltas', 'Voltas'),
                         ('Wockhardt', 'Wockhardt'),
                         ('Yes Bank', 'Yes Bank')]
    STRATEGY = [
        ('44MA', '44MA'),
        ('50MA+LBB', '50MA+LBB'),
        ('50MA+UBB', '50MA+UBB'),
        ('SUPER-T+CCI', 'SUPER-T+CCI'),
        ('OTHER', 'OTHER'),
        ('FIBONACCI','FIBONACCI')
    ]
    EMOTIONS = [
        ('NORMAL', 'NORMAL'),
        ('BALANCE', 'BALANCE'),
        ('HAPPY', 'HAPPY'),
    ]
    TRADE_TYPE = [
        ('INTRADAY', 'INTRADAY'),
        ('SWING', 'SWING'),
        ('POSITIONAL', 'POSITIONAL')
    ]
    MISTAKES = [
        ('WRONG_PREDICTION', 'WRONG_PREDICTION'),
        ('SYSTEMLESS_TRADE', 'SYSTEMLESS_TRADE'),
        ('NONE', 'NONE')
    ]
    user=models.CharField(max_length=20,default='false')
    portfolio = models.FloatField(default=0.0)
    stock = models.CharField(choices=NIFTY_BETA_STOCKS, max_length=50)
    stock_type = models.CharField(choices=TRADE_TYPE, max_length=10, default='SWING')
    buy_date = models.DateField(default=timezone.now)
    strategy = models.CharField(choices=STRATEGY, max_length=20, default='50MA+UBB')
    entry = models.FloatField(default=0.0)
    stoploss = models.FloatField(default=0.0)
    target = models.FloatField(default=0.0)
    quantity = models.FloatField(default=0.0)
    exit = models.FloatField(default=0.0)
    profit_loss_per_stock = models.FloatField(default=0.0)
    profile = models.FloatField(default=0.0)
    emotion = models.CharField(max_length=10, choices=EMOTIONS, default='NORMAL')
    mistake = models.CharField(max_length=20, choices=MISTAKES, default='NONE')
    graph = models.ImageField(upload_to='graph', blank=True)

    def __str__(self):
        return self.stock



