import streamlit as st
from functions.funcaoPlot import plot

st.title ("histórico de cotações")

st.write ("Veja o o histórico de cotações em empresas.")

ticker = st.sidebar.text_input ('Escolha o ticket: ', value = "AAPL")

fig = plot(ticker)
st.plotly_chart(fig)