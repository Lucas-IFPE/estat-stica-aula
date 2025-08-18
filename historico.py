import yfinance as yf
import plotly.express as px

data = yf.download('AAPL', period = 'max', multi_level_index = False) 

df = data.reset_index()[['Date', 'Close']]

fig = px.line(df, x = 'Date', y = 'Close')