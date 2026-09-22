"""
BQ: Are denial rates increasing over time?
Use: 04_denial_rate_trend.sql
Test: Linear Regression
    H0: No trend exists.
    H1: A significant trend exists.
"""

import pandas as pd
from scipy.stats import linregress

df = pd.read_csv("data/cleaned/healthcare_claims_cleaned.csv")
df["service_date"] = pd.to_datetime(df["service_date"])
df["month"] = df["service_date"].dt.to_period("M").astype(str)

monthly = df.groupby("month")["denial_flag"].mean().reset_index()
monthly["month_num"] = range(len(monthly))

result = linregress(monthly["month_num"], monthly["denial_flag"])

print(result)
print(result.pvalue)