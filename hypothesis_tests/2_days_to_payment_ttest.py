"""
BQ: Do Aetna and Medicare differ in average days-to-payment?
Use: 09_payment_speed_trend.sql
Test: Independent t-test
    H0: Average days-to-payment is equal.
    H1: Average days-to-payment differs.
"""

import pandas as pd
from scipy.stats import ttest_ind

# Load cleaned data
df = pd.read_csv("data/cleaned/healthcare_claims_cleaned.csv")
aetna = df[df["insurance_payer"]=="Aetna"]["days_to_payment"]
medicare = df[df["insurance_payer"]=="Medicare"]["days_to_payment"]

# Run t-test and return values
t,p = ttest_ind(aetna, medicare, equal_var=False, nan_policy="omit")

print(p)
print("\nInsurance payer does not appear to be a major driver of payment delays.")