import pandas as pd
from scripts.utils import load_sql

def get_denial_report(engine):

    denial_df = pd.read_sql(
        load_sql("queries/denials/03_denial_by_department.sql"),
        engine
    )

    denial_trend_df = pd.read_sql(
        load_sql("queries/denials/04_denial_rate_trend.sql"),
        engine
    )

    return denial_df, denial_trend_df