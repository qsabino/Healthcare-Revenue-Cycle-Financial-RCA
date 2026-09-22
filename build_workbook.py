def build_workbook():
    import pandas as pd
    from scripts.utils import get_engine
    from reports.executive_report import get_executive_report
    from reports.denial_rca_report import get_denial_report
    from reports.ar_collections_report import get_ar_report
    from reports.monthly_close_report import get_monthly_close_report
    from reports.department_performance_report import get_department_report
  
    # --------------DATABASE CONNECTION--------------
    engine = get_engine()


    # --------------GET REPORT DATA--------------
    executive_df, rca_df = get_executive_report(engine)
    denial_df, denial_trend_df = get_denial_report(engine)
    ar_df, variance_df, speed_df = get_ar_report(engine)
    monthly_df, mom_df = get_monthly_close_report(engine)
    kpi_df, dept_trend_df = get_department_report(engine)

    
    # --------------CREATE WORKBOOK--------------
    with pd.ExcelWriter(
        "output/healthcare_rca_dashboard.xlsx",
        engine="xlsxwriter"
    ) as writer:
        
        # Executive Summary
        executive_df.to_excel(writer, sheet_name="Executive Summary", startrow=0, index=False)
        rca_df.to_excel(writer, sheet_name="Executive Summary", startrow=20, index=False)
        
        # Denial RCA
        denial_df.to_excel(writer, sheet_name="Denial RCA", startrow=0, index=False)
        denial_trend_df.to_excel(writer, sheet_name="Denial RCA", startrow=15, index=False)
        
        # AR & Collections
        ar_df.to_excel(writer, sheet_name="AR & Collections", startrow=0, index=False)
        variance_df.to_excel(writer, sheet_name="AR & Collections", startrow=15, index=False )
        speed_df.to_excel(writer, sheet_name="AR & Collections", startrow=30, index=False)
        
        # Monthly Close
        monthly_df.to_excel(writer, sheet_name="Monthly Close", startrow=0, index=False)
        mom_df.to_excel(writer, sheet_name="Monthly Close", startrow=20, index=False)
        
        # Department Performance
        kpi_df.to_excel(writer, sheet_name="Department Performance", startrow=0, index=False)
        dept_trend_df.to_excel(writer, sheet_name="Department Performance", startrow=20, index=False)
        
        # FORMAT WORKSHEETS
        for sheet_name in writer.sheets:
            worksheet = writer.sheets[sheet_name]
            worksheet.freeze_panes(1, 0)
            worksheet.set_column(0, 20, 18)     
    print("Workbook created successfully.")