import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
import dash
import dash_core_components as dcc
import dash_html_components as html

spy = yf.Ticker("ES=F")
hist = spy.history(period="3d", interval="15m")

candlestick = go.Candlestick(
                            x=hist.index,
                            open=hist['Open'],
                            high=hist['High'],
                            low=hist['Low'],
                            close=hist['Close']
                            )

fig = go.Figure(data=[candlestick])

fig.update_layout(
    title = 'ES Futures Price',
    updatemenus = [
        dict(
            type="buttons",

        )
    ]
)

fig.show()