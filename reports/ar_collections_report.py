import pandas as pd
from scripts.utils import load_sql

def get_ar_report(engine):

    ar_df = pd.read_sql(
        load_sql("queries/finance/05_ar_aging.sql"),
        engine
    )

    variance_df = pd.read_sql(
        load_sql("queries/finance/06_payment_variance.sql"),
        engine
    )

    speed_df = pd.read_sql(
        load_sql("queries/finance/09_days_to_payment_trend.sql"),
        engine
    )

    return ar_df, variance_df, speed_df