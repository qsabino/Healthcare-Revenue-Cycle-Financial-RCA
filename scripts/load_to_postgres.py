import pandas as pd
from scripts.utils import get_engine

def load_to_postgres():
    
    # --------------LOAD CLEAN DATA--------------
    df = pd.read_csv("data/cleaned/healthcare_claims_cleaned.csv")


    # --------------DATABASE CONNECTION--------------
    engine = get_engine()


    # --------------CREATE DIMENSION TABLES--------------
    # dim_department
    dim_department = df[["department"]].drop_duplicates().reset_index(drop=True)
    dim_department["department_id"] = dim_department.index + 1
    
    # dim_payer
    dim_payer = df[["insurance_payer"]].drop_duplicates().reset_index(drop=True)
    dim_payer["payer_id"] = dim_payer.index + 1

    # dim_provider
    dim_provider = df[["provider_id"]].drop_duplicates().reset_index(drop=True)
    

    # --------------BUILD FACT TABLE--------------
    fact_claims = df.merge(dim_department, on="department", how="left")
    fact_claims = fact_claims.merge(dim_payer, on="insurance_payer", how="left")


    # --------------EXPORT TO POSTGRESQL--------------
    tables = {
        "dim_department": dim_department,
        "dim_payer": dim_payer,
        "dim_provider": dim_provider,
        "fact_claims": fact_claims
    }

    for name, df in tables.items():
        df.to_sql(name, engine, if_exists="replace", index=False)
        print(f"{name} loaded.")

    print("All tables loaded successfully.")