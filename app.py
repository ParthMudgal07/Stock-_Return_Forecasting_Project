import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="AMZN Return Forecast",
    page_icon="📈",
    layout="centered",
)

# ---------------------------
# Global style tweaks
# ---------------------------
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        h1, h2, h3 {
            font-weight: 600;
        }
        .metric-label {
            font-size: 0.9rem;
            color: #6b7280;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Title
# ---------------------------
st.markdown("## 📈 Amazon (AMZN)")
st.markdown(
    "Probabilistic short-term return forecast using quantile regression."
)

# ---------------------------
# Load data
# ---------------------------
df = pd.read_csv("amzn_features_final.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# ---------------------------
# Final ML output (static demo values)
# Replace with your actual final_output values
# ---------------------------
final_output = {
    "median_return_%": 0.84,
    "lower_price": 172.30,
    "upper_price": 181.90,
}

# ---------------------------
# Automated interpretation
# ---------------------------
def generate_automated_response(
    stock,
    horizon,
    median_return_pct,
    lower_price,
    upper_price,
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
        f"Over the {horizon}, {stock} is expected to show a **{bias} bias**, "
        f"with a median projected return of **{median_return_pct:.2f}%**. "
        f"The expected price range lies between **{lower_price:.2f}** and "
        f"**{upper_price:.2f}**, indicating **{uncertainty} uncertainty** "
        f"in short-term price movements."
    )

# ---------------------------
# Summary card
# ---------------------------
with st.container():
    st.markdown("### 🧠 Market Summary")
    st.markdown(
        generate_automated_response(
            stock="Amazon (AMZN)",
            horizon="next 5 trading days",
            median_return_pct=final_output["median_return_%"],
            lower_price=final_output["lower_price"],
            upper_price=final_output["upper_price"],
        )
    )

# ---------------------------
# Metrics row
# ---------------------------
st.markdown("### 📊 Forecast Snapshot")

c1, c2, c3 = st.columns(3)

c1.metric(
    label="Median Return",
    value=f"{final_output['median_return_%']:.2f}%",
)

c2.metric(
    label="Lower Price Bound",
    value=f"${final_output['lower_price']:.2f}",
)

c3.metric(
    label="Upper Price Bound",
    value=f"${final_output['upper_price']:.2f}",
)

# ---------------------------
# Price trend plot
# ---------------------------
st.markdown("### 📈 Recent Price Trend")

fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(df["Date"], df["Close"], linewidth=2)
ax.set_xlabel("")
ax.set_ylabel("Price")
ax.grid(alpha=0.2)

st.pyplot(fig, use_container_width=True)

# ---------------------------
# Volatility plot
# ---------------------------
st.markdown("### 📉 Volatility Context (20-day)")

fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(df["Date"], df["vol_20d"], linewidth=2)
ax.set_xlabel("")
ax.set_ylabel("Volatility")
ax.grid(alpha=0.2)

st.pyplot(fig, use_container_width=True)

# ---------------------------
# Return distribution plot
# ---------------------------
st.markdown("### 📊 5-Day Return Distribution")

fig, ax = plt.subplots(figsize=(6, 3))
ax.hist(
    df["future_5d_return"],
    bins=50,
    alpha=0.75,
)
ax.axvline(0, linestyle="--", linewidth=1)
ax.set_xlabel("5-Day Return")
ax.set_ylabel("Frequency")
ax.grid(alpha=0.2)

st.pyplot(fig, use_container_width=True)

# ---------------------------
# Footer note
# ---------------------------
st.markdown(
    """
    <hr>
    <small>
    Forecasts are probabilistic and based on historical price behavior.
    This dashboard is for educational purposes only.
    </small>
    """,
    unsafe_allow_html=True,
)
