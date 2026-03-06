import datetime as dt
import yfinance as yf
import pandas as pd
import numpy as np
forex= ["EURUSD=X","GBPUSD=X","GBPEUR=X"]
ohlc_data={}
for f in forex:
    temp=yf.download(f,period="1mo",interval="30m")
    ohlc_data[f]=temp
def RSI(DF,n=14):
    df=DF.copy()
    df["change"]=df["Close"]-df["Close"].shift(1)
    df["gain"]=np.where(df["change"]>=0,df["change"],0)
    df["loss"] = np.where(df["change"] < 0,-1* df["change"], 0)
    df["avg_gain"]=df["gain"].ewm(alpha=1/n,min_periods=n).mean()
    df["avg_loss"]=df["loss"].ewm(alpha=1/n,min_periods=n).mean()
    df["rs"]=df["avg_gain"]/df["avg_loss"]
    df["rsi"]=100-(100/(1+df["rs"]))
    return df["rsi"]
for f in ohlc_data:
    ohlc_data[f]["RSI"]=RSI(ohlc_data[f])