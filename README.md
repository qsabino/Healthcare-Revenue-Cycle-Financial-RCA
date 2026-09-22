# Healthcare Revenue Cycle & Financial RCA

## Project Summary

This project was created to practice the technical skills commonly used in Healthcare Revenue Cycle and Financial Analytics roles.

The workflow take a raw healthcare claims dataset, clean it, loading it into PostgreSQL, performing SQL-based root cause analysis, validating findings through statistical testing, and producing automated Excel reports.

## Business Objectives

- Identify denial trends and root causes
- Monitor Accounts Receivable (AR) aging
- Analyze payment variance and reimbursement performance
- Track department-level operational KPIs
- Support monthly financial close reporting

## Technology Stack

- Python
- PostgreSQL
- SQLAlchemy
- Pandas
- SciPy
- XlsxWriter
- OpenPyXL
- VS Code

## Project Workflow

- Receive raw healthcare claims data
- Clean and validate records
- Load dimensional and fact tables into PostgreSQL
- Perform SQL-based RCA analysis
- Conduct statistical testing (Chi-Square, T-Test, ANOVA, Regression)
- Generate automated Excel reports
- Execute the entire pipeline through a single entry point (main.py)

## Database Schema

### Fact Table
- fact_claims
  
### Dimension Tables
- dim_department
- dim_payer
- dim_provider

## Analyses Performed

### Executive Reporting

- Executive Summary Metrics
- Top Revenue Cycle Drivers
  
### Denial Management

- Denial Trends by Department
- Denial Rate Trend Analysis
  
### Finance & Collections

- AR Aging Analysis
- Payment Variance Analysis
- Payment Speed Trend Analysis

### Financial Reporting

- Monthly Close Reporting
- Month-over-Month Variance Analysis
  
### Operations

- Department KPI Monitoring
- Department Performance Trends

## Statistical Testing

- Chi-Square Test
- Independent Two-Sample T-Test
- One-Way ANOVA
- Regression

## Automated Reporting

The project generates a multi-sheet Excel workbook containing:

- Executive Summary
- Denial RCA
- AR & Collections
- Monthly Close
- Department Performance

## Run the Project
- pip install -r requirements.txt
- python main.py
<img width="1318" height="661" alt="image" src="https://github.com/user-attachments/assets/20e6db35-49a8-4be9-bb28-dc39844414e4" />
