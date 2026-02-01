Probabilistic Stock Return Forecasting (Amazon)

Overview

This project builds a probabilistic stock return forecasting system for Amazon (AMZN) using historical price data.
The system estimates:

Median expected return (%) over the next 5 trading days

A price range capturing downside and upside uncertainty using quantile regression

The final outputs are presented through an interactive Streamlit dashboard along with a market summary.

Problem Statement

Traditional stock price prediction models often aim to forecast a single future price, which can be misleading due to market uncertainty and volatility.

This project addresses that limitation by:

Modeling return distributions instead of point estimates

Quantifying uncertainty using quantile regression

Presenting outputs in a risk aware and interpretable format

Data Source

Historical OHLCV data for Amazon (AMZN)

Data obtained from Yahoo Finance

Time period: Multi-year historical data (used for training and testing)

Methodology
1. Exploratory Data Analysis 

Price trends and return distributions

Volatility analysis

Autocorrelation analysis

Identification of useful predictive signals

2. Feature Engineering

Key features derived from OHLCV data:

Momentum features (5, 10, 20-day returns)

Volatility features (rolling standard deviation)

Volume based features

Lagged features

Technical indicators 

Target variable:

Future 5-day return

3. Modeling Approach

Quantile Regression using Gradient Boosting

Separate models trained for:

10th percentile (q10)

50th percentile (q50 – median)

90th percentile (q90)

This allows the model to estimate the full conditional distribution of future returns.

4. Model Evaluation

Quantile coverage analysis to assess calibration

Validation that:

~10% of actual returns fall below q10

~50% fall below q50

~90% fall below q90

This ensures the probabilistic forecasts are well calibrated.

5. Final Model Output

For the most recent observation:

Median expected return (%)

Expected price range, computed as:

Lower bound → q10

Upper bound → q90

Interpretation Layer

The project uses a deterministic interpretation engine that converts numerical model outputs into a clear market summary.

Streamlit Dashboard

The dashboard presents:

Market summary

Median return and price range

Recent price trend

Volatility context

Distribution of historical 5-day returns

Run the Dashboard
streamlit run app.py

Assumptions & Limitations

Model relies solely on historical price and volume data

No fundamental, macroeconomic, or news based inputs

Performance may degrade during extreme market events

Outputs are not investment advice

Key Takeaways

Predicting ranges and probabilities is more informative than predicting exact prices

Quantile regression provides a natural framework for uncertainty modeling

Separating modeling from presentation improves system design and clarity

Technologies Used

Python

Pandas, NumPy

Scikit-learn

Matplotlib

Streamlit

Future Enhancements

Extend to multiple stocks

Add regime detection

Incorporate additional data sources

Enable dynamic stock selection in the dashboard

Disclaimer

This project is for educational purposes only and does not constitute financial or investment advice.
