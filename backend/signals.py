import yfinance as yf
import pandas as pd
import ta

symbols = [
    "BTC-USD","ETH-USD","BNB-USD","XRP-USD","ADA-USD","SOL-USD","DOGE-USD","MATIC-USD",
    "DOT-USD","LTC-USD","TRX-USD","AVAX-USD","SHIB-USD","ATOM-USD","LINK-USD",
    "AAPL","TSLA","AMZN","GOOGL","META","NVDA","MSFT","NFLX","PYPL","AMD"
]

def get_signal(data):
    close = data["Close"]
    rsi = ta.momentum.RSIIndicator(close).rsi().iloc[-1]
    ema_short = ta.trend.EMAIndicator(close, window=9).ema_indicator().iloc[-1]
    ema_long = ta.trend.EMAIndicator(close, window=21).ema_indicator().iloc[-1]

    if rsi < 30 and ema_short > ema_long:
        return "BUY"
    elif rsi > 70 and ema_short < ema_long:
        return "SELL"
    else:
        return "HOLD"

def get_all_signals():
    results = []
    for sym in symbols:
        try:
            df = yf.download(sym, period="5d", interval="1h")
            sig = get_signal(df)
            results.append({"symbol": sym, "signal": sig})
        except:
            pass
    return results
