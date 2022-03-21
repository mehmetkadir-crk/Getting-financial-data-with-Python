from cProfile import label
from operator import index
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Pandas ile verileri okuduk
AAPL = pd.read_csv("AAPL.csv")
#print(AAPL.head())

#30 Günlük hareketli ortalama
SMA30 = pd.DataFrame() #Yeni dataset oluşturduk
SMA30 ['Deger'] = AAPL['Close'].rolling(window=20).mean() #Günlerin son 30 günlük ortalamasını aldık

#30 Günlük hareketli ortalama
SMA100 = pd.DataFrame()
SMA100 ['Deger'] = AAPL['Close'].rolling(window=200).mean() #Günlerin son 100 günlük ortalamasını aldık

#Verilerin hepsini bir veri setine topladık
veriseti = pd.DataFrame()
veriseti['Tarih'] = AAPL['Date']
veriseti['Fiyat'] = AAPL['Close']
veriseti['SMA30'] = SMA30['Deger']
veriseti['SMA100'] = SMA100['Deger']

#Al- Sat Fonksiyonu
def al_sat(veri):
    sinyal_Al = []
    sinyal_Sat = []
    bayrak = -1

    for i in range(len(veri)):

        if (veri['SMA30'][i] > veri['SMA100'][i]) & (bayrak != 1): #30 günlük ortalama 100 günlükten büyükse
            sinyal_Al.append(veri['Fiyat'][i]) #Al sinyaline o günkü fiyatı ekle
            sinyal_Sat.append(np.nan) #NaN değerini ekle
            bayrak = 1
        
        elif (veri['SMA30'][i] < veri['SMA100'][i]) & (bayrak != 0): #30 günlük ortalama 100 günlükten küçükse
            sinyal_Al.append(np.nan) #NaN değerini ekle
            sinyal_Sat.append(veri['Fiyat'][i]) #Sat sinyaline o günkü fiyatı ekle
            bayrak = 0
        
        else:
            sinyal_Al.append(np.nan) #NaN değerini ekle
            sinyal_Sat.append(np.nan) #NaN değerini ekle
        
    return (sinyal_Al, sinyal_Sat)

#"veriseti"ni, al_sat fonksiyonuna soktuk ve çıkan Al, Sat değerlerini "al_sat_dataset"e aktardık
al_sat_dataset = al_sat(veriseti)
#al_sat_dataset içinde bulunan değerleri, "veriseti"ne tekrar aktardık
veriseti['Al_Sinyal_Degeri'] = al_sat_dataset[0]
veriseti['Sat_Sinyal_Degeri'] = al_sat_dataset[1]

plt.figure(figsize=(15, 10)) #Grafiğin, inç cinsinden boyutu
plt.plot(veriseti['Fiyat'], label ='AAPL')
plt.plot(veriseti['SMA30'], label ='SMA30')
plt.plot(veriseti['SMA100'], label ='SMA100')
#Scater = işaretlenmiş nokta olarak gösterimi yapar (Al/Sat yapılacak yerleri nokta olarak göstermek için)
plt.scatter(veriseti.index, veriseti['Al_Sinyal_Degeri'], label = 'Al', marker = '*', color = 'green') 
plt.scatter(veriseti.index, veriseti['Sat_Sinyal_Degeri'], label = 'Sat', marker = '*', color = 'red')
plt.legend(loc = 'upper left') #grafiğin sol üst tarafına, şekillerin açıklamasını (label) ekler
plt.title('Apple Hisse Verisi')
plt.xlabel('Tarih')
plt.ylabel('Fiyat (USD)')

plt.show()