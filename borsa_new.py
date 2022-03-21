from math import degrees
import time #Tarih için eklendi
import datetime
import pandas as pd #csv ye aktarmak için ekledik

etiket = 'AAPL' #Paritenin Yahoo Finance etiketi

zaman1 = int(time.mktime(datetime.datetime(2010, 3, 3, 23, 59).timetuple())) #Başlangıç

zaman2 = int(time.mktime(datetime.datetime(2022, 3, 3, 23, 59).timetuple())) #Bitiş
sure = '1d' # 1d, 1m

#Yahoo Finace dan belirlediğimiz paritenin linkini kopyaladık
#Paritenin verileri "deger" setine eklendi
deger = f'https://query1.finance.yahoo.com/v7/finance/download/{etiket}?period1={zaman1}&period2={zaman2}&interval={sure}&events=history&includeAdjustedClose=true'

#veriler degiskenine, aldığımız verileri ekledik
veriler = pd.read_csv(deger)

#Veri setini, AAPL adında csv dosyasına aktardık
veriler.to_csv('AAPL.csv')