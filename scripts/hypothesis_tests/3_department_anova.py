"""
BQ: Do departments differ in reimbursement performance?
Use: 10_department_kpis.sql
Test: One-Way ANOVA
    H0: All departments have the same mean reimbursement ratio.
    H1: At least one department differs.
"""

import pandas as pd

from scipy.stats import f_oneway

# Load cleaned data

df = pd.read_csv(
    "data/cleaned/healthcare_claims_cleaned.csv"
)

groups = [

    grp["reimbursement_ratio"].dropna()

    for _, grp in df.groupby("department")

]

f,p = f_oneway(*groups)

print(f)
print(p)

print("\nDepartment does not appear to be a major driver of reimbursement performance.")
