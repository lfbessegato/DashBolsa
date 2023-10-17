import yfinance as yf
import streamlit as st
st.set_page_config(
    page_title = 'DASHBOARD FINANCEIRO - AÇÕES',
    layout='wide'
)
st.header('FECHAMENTO E DIVIDENDO DE AÇÕES')

ticker = st.text_input('Digite o ticker da ação', 'PETR4')
empresa = yf.Ticker(f"{ticker}.SA")
tickerDF = empresa.history(period='1d', start='2023-01-01', end='2023-10-13')

# Definir a proporção
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.write(f"**Empresa:** {empresa.info['longName']}")
with col2:
    st.write(f"**Mercado:** {empresa.info['industryDisp']}")
with col3:
    st.write(f"**Preço Atual:** {empresa.info['currentPrice']} BRL")

st.line_chart(tickerDF.Close)
st.bar_chart(tickerDF.Dividends)