import pandas as pd
from scripts.utils import load_sql

def get_monthly_close_report(engine):
    
    monthly_df = pd.read_sql(
        load_sql("queries/finance/07_monthly_close.sql"),
        engine
    )

    mom_df = pd.read_sql(
        load_sql("queries/finance/08_mom_variance.sql"),
        engine
    )

    return monthly_df, mom_df