**Stock Return Forecasting Dashboard**
<img width="1110" height="724" alt="image" src="https://github.com/user-attachments/assets/c84aaae5-0662-4fe7-b1f9-46d6128c74bd" />
Dasboard Link: https://stock-return-forecasting-project.streamlit.app/
**Overview**

This project builds a probabilistic short term stock return forecasting system for Amazon (AMZN) using historical market data.

The model estimates:

The median expected return (%)

A price range representing downside and upside risk using quantile regression

The final results are presented through an interactive Streamlit dashboard with a clean, minimal UI and a market summary.

Motivation

Stock prices are inherently uncertain. Point predictions often hide risk and give a false sense of precision.

This project focuses on:

Modeling uncertainty explicitly

Predicting return distributions

Presenting results in a risk aware and interpretable manner

Data Source

Amazon (AMZN) historical OHLCV data

Sourced from Yahoo Finance

Multi year daily price history

Project Structure

├── EDA.ipynb
│   └── Exploratory data analysis:
│       - Price trends
│       - Return distributions
│       - Volatility analysis
│       - Autocorrelation analysis
│
├── Feature_engineering.ipynb
│   └── Feature creation:
│       - Momentum features
│       - Volatility features
│       - Volume-based features
│       - Lagged variables
│       - Technical indicators
│
├── Model_Training.ipynb
│   └── Quantile regression modeling:
│       - q10 (downside risk)
│       - q50 (median return)
│       - q90 (upside potential)
│       - Calibration & coverage evaluation
│
├── app.py
│   └── Streamlit dashboard:
│       - Automated market summary
│       - Forecast metrics
│       - Visual analytics
│
├── amzn_data.csv
│   └── Raw historical price data
│
├── amzn_features_final.csv
│   └── Feature-engineered dataset used for modeling
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md

**Methodology**
Exploratory Data Analysis (EDA)

Examined price trends and regime behavior

Analyzed daily and multi-day return distributions

Studied volatility clustering and autocorrelation

Identified signals useful for short-term forecasting

**Feature Engineering**

Derived predictive features from raw OHLCV data:

Momentum (5, 10, 20-day returns)

Rolling volatility measures

Volume change and ratios

Lagged features

Technical indicators (e.g., RSI)

Target Variable:

Future 5-day return

**Modeling Approach**

Quantile Regression using Gradient Boosting

Separate models trained for:

q10 → downside risk

q50 → median expected return

q90 → upside potential

This allows the model to estimate a conditional return distribution rather than a single value.

**Model Evaluation**

Evaluated quantile coverage on the test set

Verified that predicted quantiles are well-calibrated

Ensured probabilistic outputs are statistically meaningful

Final Model Output

For the most recent observation:

Median expected return (%)

Expected price range

Lower bound → q10

Upper bound → q90

These outputs are probabilistic, not deterministic.

**Streamlit Dashboard**

The Streamlit app provides:

Automated market summary

Median return and price range

Recent price trend visualization

Volatility context

Historical return distribution

Technologies Used

Python

Pandas, NumPy

Scikit-learn

Matplotlib

Streamlit

Disclaimer

This project is for educational and demonstrative purposes only and does not constitute financial or investment advice.
