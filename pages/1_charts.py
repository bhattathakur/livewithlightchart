# import pandas as pd
# from lightweight_charts import Chart


# if __name__ == '__main__':
    
#     chart = Chart()
    
#     # Columns: time | open | high | low | close | volume 
#     df = pd.read_csv('ohlcv.csv')
#     chart.set(df)
    
#     chart.show(block=True)

import pandas as pd
import streamlit as st
import plotly.graph_objects as go
# Set page layout to wide and no sidebar
st.set_page_config(layout="wide", page_title="Full Window OHLCV Chart")

df = pd.read_csv('ohlcv.csv')

fig = go.Figure(data=[go.Candlestick(
    x=df['date'],
    open=df['open'],
    high=df['high'],
    low=df['low'],
    close=df['close']
)])

st.title("OHLCV Candlestick Chart")
st.plotly_chart(fig, use_container_width=True)
