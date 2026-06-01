import pandas as pd
from scripts.utils import load_sql

def get_department_report(engine):

    kpis_df = pd.read_sql(
        load_sql("queries/operation/10_department_kpis.sql"),
        engine
    )

    dept_trend_df = pd.read_sql(
        load_sql("queries/operation/11_department_performance_trend.sql"),
        engine
    )

    return kpis_df, dept_trend_df