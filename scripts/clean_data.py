import pandas as pd
import numpy as np
from pathlib import Path

def clean_data():

    # --------------LOAD RAW DATA--------------
    input_path = Path("data/raw/healthcare_claims_raw.csv")
    df = pd.read_csv(input_path)
    print(f"Raw data loaded: {df.shape}")
    

    # --------------REMOVE DUPLICATES--------------
    before = len(df)
    df = df.drop_duplicates(subset="claim_id")
    after = len(df)
    print(f"Removed {before - after} duplicate claims.")


    #--------------STANDARDIZE TEXT--------------
    text_columns = ["department", "insurance_payer", "location", "claim_status"]
    for col in text_columns:
        df[col] = df[col].astype(str).str.strip().str.title()


    # --------------FIX NEGATIVE PAYMENTS--------------
    negative_count = (df["paid_amount"] < 0).sum()
    df.loc[df["paid_amount"] < 0, "paid_amount"] = np.nan
    print(f"Fixed {negative_count} negative payments.")


    # --------------DATE CONVERSION--------------
    date_columns = ["service_date", "billing_date", "payment_date"]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")


    # --------------INVALID PAYMENT DATES--------------
    invalid_dates = (df["payment_date"] < df["billing_date"])
    invalid_count = invalid_dates.sum()
    df.loc[invalid_dates, "payment_date"] = pd.NaT
    print(f"Fixed {invalid_count} invalid payment dates.")

 
    # --------------REBUILD DAYS TO PAYMENT--------------
    df["days_to_payment"] = (df["payment_date"] - df["billing_date"]).dt.days


    # --------------HANDLE MISSING PAYERS--------------
    df["insurance_payer"] = df["insurance_payer"].replace({"Nan": "Unknown", "": "Unknown"})


    # --------------CREATE PAYMENT VARIANCE--------------
    df["payment_variance"] = (df["claim_amount"] - df["paid_amount"]).round(2)


    # --------------CREATE REIMBURSEMENT RATIO--------------
    df["reimbursement_ratio"] = (df["paid_amount"] / df["claim_amount"]).round(2)


    # --------------CREATE AR AGING BUCKETS--------------
    df["aging_bucket"] = pd.cut(
        df["days_to_payment"],
        bins=[0,30,60,90,999],
        labels=["0-30", "31-60", "61-90", "90+"]
    )


    # --------------OUTLIER FLAGGING--------------
    threshold = df["claim_amount"].quantile(0.99)
    df["high_claim_flag"] = np.where(df["claim_amount"] > threshold, 1, 0)
    print(f"Outlier threshold: {threshold}")


    # --------------FINAL QA CHECKS--------------
    print(f"Missing Values: {df.isnull().sum()}")
    print("Final Shape: {df.shape}")

    
    # --------------EXPORT CLEAN DATA--------------
    output_path = Path("data/cleaned")
    output_path.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path/"healthcare_claims_cleaned.csv", index=False)
    print("\nCleaned data exported.")