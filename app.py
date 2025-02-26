import streamlit as st
import pandas as pd
import requests

# Define your portfolio with asset, size, and entry price
portfolio = [
    {"asset": "bitcoin", "symbol": "btc", "size": 0.05, "entry_price": 45000},
    {"asset": "ethereum", "symbol": "eth", "size": 1.2, "entry_price": 3000},
    {"asset": "solana", "symbol": "sol", "size": 10, "entry_price": 150}
]


# Function to get live crypto prices from CoinGecko
def get_live_price(symbol):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
        response = requests.get(url).json()
        return response[symbol]["usd"] if symbol in response else None
    except Exception as e:
        st.error(f"Error fetching price for {symbol}: {e}")
        return None


# Streamlit UI
st.title("📊 Crypto Portfolio Tracker")
st.write("Track your crypto investments in real-time.")

# Create DataFrame to store portfolio data
df = pd.DataFrame(portfolio)

# Fetch live prices and calculate portfolio performance
for index, row in df.iterrows():
    live_price = get_live_price(row["asset"])
    if live_price:
        df.at[index, "Current Price"] = live_price
        df.at[index, "Current Value ($)"] = row["size"] * live_price
        df.at[index, "Profit/Loss ($)"] = (live_price - row["entry_price"]) * row["size"]
    else:
        df.at[index, "Current Price"] = "N/A"
        df.at[index, "Current Value ($)"] = "N/A"
        df.at[index, "Profit/Loss ($)"] = "N/A"

# Display portfolio table
st.dataframe(df)

# Show total portfolio value
total_value = df["Current Value ($)"].replace("N/A", 0).sum()
st.subheader(f"💰 Total Portfolio Value: **${total_value:,.2f}**")
