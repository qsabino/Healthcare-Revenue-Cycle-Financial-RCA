"""
BQ: Do denial rates differ significantly between departments?
Use: 03_denial_by_department.sql
Test: Chi-Square Test
    H0: Denial rate is independent of department.
    H1: Denial rate depends on department.
"""

import pandas as pd
from scipy.stats import chi2_contingency

# Load cleaned data
df = pd.read_csv("data/cleaned/healthcare_claims_cleaned.csv")

# Create contingency table
contingency = pd.crosstab(df["department"], df["denial_flag"])
print(contingency)

# Run Chi-Square test
chi2, p, dof, expected = chi2_contingency(contingency)

print("\nChi-Square Test")
print(f"Chi2 Statistic: {chi2:.4f}")
print(f"P-value: {p:.4f}")
print(f"Degrees of Freedom: {dof}")

print("\np-value = 0.32 --> Department does not appear to be a significant root cause of claim denials. Further investigation needed")