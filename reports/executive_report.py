import pandas as pd
from scripts.utils import load_sql

def get_executive_report(engine):
    executive_df = pd.read_sql(
        load_sql("queries/executive/01_executive_summary.sql"),
        engine
    )
    rca_df = pd.read_sql(
        load_sql("queries/executive/02_top_rca_drivers.sql"),
        engine
    )
    return executive_df, rca_df