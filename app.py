import streamlit as st
import pandas
import yfinance as yf

st.title("Stock viewer")

tick = st.text_input("What stock would you like to view? (enter the ticker)").upper()

data = yf.download(tick)

st.write(data)


