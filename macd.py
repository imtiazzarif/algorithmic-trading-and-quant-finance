import datetime as dt
import yfinance as yf
import pandas as pd
import numpy as np
forex= ["EURUSD=X","GBPUSD=X","GBPEUR=X"]
ohlc_data={}
for f in forex:
    temp=yf.download(f,period="1mo",interval="15m")
    ohlc_data[f]=temp
def MACD(DF,a=12,b=26,c=9):
    df=DF.copy()
    df["ma_fast"]=df["Close"].ewm(span=a,min_periods=a).mean()
    df["ma_slow"]=df["Close"].ewm(span=b,min_periods=b).mean()
    df["macd"]=df["ma_fast"]-df["ma_slow"]
    df["signal"]=df["macd"].ewm(span=c,min_periods=c).mean()
    return df.loc[:,["macd","signal"]]
for f in forex:
    ohlc_data[f][["MACD","SIGNAL"]]=MACD(ohlc_data[f])


