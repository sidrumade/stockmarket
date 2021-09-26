from django.shortcuts import render
from django.http import HttpResponse
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotSelectableException, TimeoutException
import itertools
import datetime
from time import sleep
import base64
from sendgrid import *
from sendgrid.helpers.mail import Mail
# Create your views here.

def mailing(request,key):
    print('key========',key)
    commands=['mkdir stocks','rm -rf stocks']
    try:
        os.system(commands[0])
    except Exception as e:
        print('error',e)

    obj=SendMail()
    obj._load_df_()
    obj._fetch_images_()
    resp=obj._send_()


    try:
        os.system(commands[1])
    except Exception as e:
        print('error',e)

    if resp == 'success':
        return HttpResponse('success')
    else:
        return HttpResponse('faild')
class SendMail:
    def __init__(self):
        self.df=None
        self.date=str(datetime.datetime.today().date())
        print('Main Function Started')

    def _load_df_(self):
        self.df=pd.read_csv('symbols.csv')
        print(self.df)
        print('csv loaded')
    def _fetch_images_(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        #wd = webdriver.Chrome(os.getcwd()+'/chromedriver',options=options)
        print('os.getcwd() ---',os.getcwd())
        print('os.listdir()---',os.listdir())
        
        driver =webdriver.Chrome('./chromedriver',options=options) #apply / accordingly win/linux for server its diff
        driver.set_window_size(1920, 1080)
        driver.fullscreen_window()
        count=itertools.count()
        for symbol in self.df['Symbol'][:2]:
            print(f'{next(count)} getting symbol: {symbol}' )
            driver.get(f"https://www.tradingview.com/chart/qfAlyneT/?symbol=NSE%3A{symbol}")
            sleep(5)
            driver.save_screenshot(f"stocks/{symbol}{self.date}.png")
        print('successfully symbol chart downloaded')
    def _attach_images_(self,message):
        for symbol in self.df['Symbol'][:2]:
            f=open(f"stocks/{symbol}{self.date}.png", 'rb') 
            data = f.read()
            f.close()
            encoded_file = base64.b64encode(data).decode()
            attachedFile = Attachment(
            FileContent(encoded_file),
            FileName(f'{symbol}-{self.date}.png'),
            FileType('image/png'),
            Disposition('attachment')
            )
            message.add_attachment(attachedFile)
            print(f'attaching {symbol}')
    def _send_mail_(self,from_email='siddhesh.rumade.4@gmail.com',to_email='siddhesh.rumade.5@gmail.com',subject='test',html='test',from_name='Siddhesh Rumade',attachments={}):
        message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=html)
        try:
            api='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'
            sg = SendGridAPIClient(api)
            self._attach_images_(message) #attach images
            print('attachment done')
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            return 'success'
        except Exception as e:
            print(e.message)
            return 'faild'
    def _send_(self):
        html="""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
        <h1>Stocks Today </h1>
        </body>
        </html>
        """

        # send_mail(html=email_text)
        return self._send_mail_(html=html)


