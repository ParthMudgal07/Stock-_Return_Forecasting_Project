import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Amazon Return Forecast",
    page_icon="",
    layout="centered",
)

# ---------------------------
# Custom CSS (Premium Minimal Theme)
# ---------------------------
st.markdown(
    """
    <style>
        body {
            background-color: #f9fafb;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 900px;
        }
        h1, h2, h3 {
            font-weight: 600;
            color: #111827;
        }
        p {
            color: #374151;
        }
        .card {
            background: white;
            border-radius: 14px;
            padding: 1.5rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 1.5rem;
        }
        .metric-card {
            background: white;
            border-radius: 14px;
            padding: 1rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            text-align: center;
        }
        .footer {
            font-size: 0.8rem;
            color: #6b7280;
            text-align: center;
            margin-top: 2rem;
        }
        hr {
            border: none;
            height: 1px;
            background-color: #e5e7eb;
            margin-top: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Header
# ---------------------------
st.markdown("## Amazon")
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
# Final ML output (demo values)
# ---------------------------
final_output = {
    "median_return_%": 0.84,
    "lower_price": 172.30,
    "upper_price": 181.90,
}

# ---------------------------
# Automated interpretation logic
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
        f"Over the {horizon}, {stock} is expected to show a "
        f"**{bias} bias**, with a median projected return of "
        f"**{median_return_pct:.2f}%**. The expected price range lies "
        f"between **{lower_price:.2f}** and **{upper_price:.2f}**, "
        f"indicating **{uncertainty} uncertainty** in short-term movements."
    )

# ---------------------------
# Market Summary Card
# ---------------------------
st.markdown(
    f"""
    <div class="card">
        <h3>Market Summary</h3>
        <p>{generate_automated_response(
            "Amazon (AMZN)",
            "next 5 trading days",
            final_output["median_return_%"],
            final_output["lower_price"],
            final_output["upper_price"],
        )}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Metrics
# ---------------------------
st.markdown("### Forecast Snapshot")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        f"""
        <div class="metric-card">
            <h3>{final_output['median_return_%']:.2f}%</h3>
            <p>Median Return</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        f"""
        <div class="metric-card">
            <h3>${final_output['lower_price']:.2f}</h3>
            <p>Lower Bound</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        f"""
        <div class="metric-card">
            <h3>${final_output['upper_price']:.2f}</h3>
            <p>Upper Bound</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------
# Price Trend Plot
# ---------------------------
st.markdown("### Recent Price Trend")
with st.container():
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(df["Date"], df["Close"], linewidth=2)
    ax.set_xlabel("")
    ax.set_ylabel("Price")
    ax.grid(alpha=0.2)
    st.pyplot(fig, use_container_width=True)

# ---------------------------
# Volatility Plot
# ---------------------------
st.markdown("### Volatility (20-day)")
with st.container():
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(df["Date"], df["vol_20d"], linewidth=2)
    ax.set_xlabel("")
    ax.set_ylabel("Volatility")
    ax.grid(alpha=0.2)
    st.pyplot(fig, use_container_width=True)

# ---------------------------
# Return Distribution
# ---------------------------
st.markdown("### 5-Day Return Distribution")
with st.container():
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.hist(df["future_5d_return"], bins=50, alpha=0.75)
    ax.axvline(0, linestyle="--", linewidth=1)
    ax.set_xlabel("5-Day Return")
    ax.set_ylabel("Frequency")
    ax.grid(alpha=0.2)
    st.pyplot(fig, use_container_width=True)

# ---------------------------
# Footer
# ---------------------------
st.markdown(
    """
    <hr>
    <div class="footer">
        Forecasts are probabilistic and based on historical price behavior.
        This dashboard is for educational purposes only.
    </div>
    """,
    unsafe_allow_html=True,
)
