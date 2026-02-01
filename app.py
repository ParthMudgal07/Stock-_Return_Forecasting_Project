import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Stock Forecast Dashboard",
    layout="centered"
)

st.title("Amazon Return Forecast")
st.write(
    "This dashboard presents a probabilistic forecast of Amazon's "
    "5-day return and expected price range based on historical patterns."
)

df = pd.read_csv("amzn_features_final.csv")


df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

final_ml_output = {
    "median_return_percent": 0.84,    
    "lower_price": 172.30,
    "upper_price": 181.90
}

def generate_automated_response(
    stock,
    horizon,
    median_return_pct,
    lower_price,
    upper_price
):
    if median_return_pct > 1:
        bias = "positive"
    elif median_return_pct < -1:
        bias = "negative"
    else:
        bias = "neutral"

    range_width = upper_price - lower_price
    avg_price = (upper_price + lower_price) / 2

    if range_width / avg_price > 0.08:
        uncertainty = "high"
    elif range_width / avg_price > 0.04:
        uncertainty = "moderate"
    else:
        uncertainty = "low"

    return (
        f"Over the next 5 trading days, {stock} is expected to exhibit a "
        f"{bias} bias, with the median forecast indicating a return of "
        f"approximately {median_return_pct:.2f}%. "
        f"The expected price range is between {lower_price:.2f} and "
        f"{upper_price:.2f}, suggesting {uncertainty} uncertainty "
        f"in short-term price movements."
    )


st.subheader("Market Summary")

summary = generate_automated_response(
    stock="Amazon",
    horizon="next 5 trading days",
    median_return_pct=final_ml_output["median_return_percent"],
    lower_price=final_ml_output["lower_price"],
    upper_price=final_ml_output["upper_price"]
)

st.write(summary)



st.subheader("Forecast Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Median Return (%)", f"{final_ml_output['median_return_percent']:.2f}%")
col2.metric("Lower Price Bound", f"{final_ml_output['lower_price']:.2f}")
col3.metric("Upper Price Bound", f"{final_ml_output['upper_price']:.2f}")


st.subheader("Recent Price Trend")

fig, ax = plt.subplots()
ax.plot(df["Date"], df["Close"])
ax.set_title("Amazon Closing Price")
ax.set_xlabel("Date")
ax.set_ylabel("Price")

st.pyplot(fig)


st.subheader("Market Volatility Over Time")

fig, ax = plt.subplots()
ax.plot(df["Date"], df["vol_20d"])
ax.set_title("20-Day Rolling Volatility")
ax.set_xlabel("Date")
ax.set_ylabel("Volatility")

st.pyplot(fig)


st.subheader("5-Day Return Distribution")

fig, ax = plt.subplots()
ax.hist(df["future_5d_return"], bins=50, alpha=0.7)

ax.axvline(0, color="black", linestyle="--", label="Zero Return")
ax.legend()

ax.set_title("Distribution of 5-Day Returns")
ax.set_xlabel("Return")
ax.set_ylabel("Frequency")

st.pyplot(fig)
