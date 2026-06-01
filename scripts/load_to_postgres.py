import pandas as pd

from scripts.utils import get_engine

def load_to_postgres():
    
    # -----------------------------------
    # LOAD CLEAN DATA
    # -----------------------------------

    df = pd.read_csv(
        "data/cleaned/healthcare_claims_cleaned.csv"
    )

    # -----------------------------------
    # DATABASE CONNECTION
    # -----------------------------------
  
    engine = get_engine()

    # -----------------------------------
    # CREATE DIMENSION TABLES
    # -----------------------------------

    # dim_department

    dim_department = (
        df[["department"]] # selects only the department column, double brackets keeps it as a DataFrame
        .drop_duplicates()
        .reset_index(drop=True) # resets row numbers to 0, 1, 2... drop=True means don't keep the old index as a column
    )

    dim_department["department_id"] = (
        dim_department.index + 1
    )

    # dim_payer

    dim_payer = (
        df[["insurance_payer"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    dim_payer["payer_id"] = (
        dim_payer.index + 1
    )

    # dim_provider

    dim_provider = (
        df[["provider_id"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    # -----------------------------------
    # BUILD FACT TABLE
    # -----------------------------------

    fact_claims = df.merge(
        dim_department,
        on="department",
        how="left"
    )

    fact_claims = fact_claims.merge(
        dim_payer,
        on="insurance_payer",
        how="left"
    )

    # -----------------------------------
    # EXPORT TO POSTGRESQL
    # -----------------------------------

    dim_department.to_sql(
        "dim_department",
        engine,
        if_exists="replace",
        index=False
    )

    print("dim_department loaded.")

    dim_payer.to_sql(
        "dim_payer",
        engine,
        if_exists="replace",
        index=False
    )

    print("dim_payer loaded.")

    dim_provider.to_sql(
        "dim_provider",
        engine,
        if_exists="replace",
        index=False
    )

    print("dim_provider loaded.")

    fact_claims.to_sql(
        "fact_claims",
        engine,
        if_exists="replace",
        index=False
    )

    print("fact_claims loaded.")

    print("All tables loaded successfully.")