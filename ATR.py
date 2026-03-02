import datetime as dt
import yfinance as yf
import pandas as pd
import numpy as np
forex= ["EURUSD=X","GBPUSD=X","GBPEUR=X"]
ohlc_data={}
for f in forex:
    temp=yf.download(f,period="1mo",interval="30m")
    ohlc_data[f]=temp
def ADR(DF,n=14):
    df=DF.copy()
    df["H-L"]=df["High"]-df["Low"]
    df["H-PC"]=abs(df["High"]-df["Close"].shift(1))
    df["L-PC"]=abs(df["Low"]-df["Close"].shift(1))
    df["TR"]=df[["H-L","H-PC","L-PC"]].max(axis=1,skipna=False)
    df["ATR"]=df["TR"].ewm(span=n,min_periods=n).mean()
    return df["ATR"]
for f in ohlc_data:
   ohlc_data[f]["ATR"]= ADR(ohlc_data[f])
print(ohlc_data["EURUSD=X"].tail())