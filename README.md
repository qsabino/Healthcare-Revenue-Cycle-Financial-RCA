# Healthcare Revenue Cycle Analytics

## Project Overview

This project simulates a Healthcare Revenue Cycle Analytics environment and demonstrates an end-to-end analytics workflow using Python, PostgreSQL, SQL, statistical analysis, and Excel automation.

The solution generates healthcare claims data, loads it into a relational database, performs root cause analysis (RCA), validates findings through hypothesis testing, and automatically produces executive reporting deliverables.

---

## Business Objectives

* Analyze denial trends and root causes
* Monitor Accounts Receivable (AR) aging
* Evaluate payment variance and reimbursement performance
* Track operational KPIs by department
* Support month-end financial reporting

---

## Technology Stack

* Python
* PostgreSQL
* VS Code

---

## Analytics Workflow

```text
Raw Data
      ↓
Clean Data
      ↓
Load PostgreSQL
      ↓
SQL RCA Analysis
      ↓
Hypothesis Testing
      ↓
Excel Reporting
      ↓
Automated Pipeline (main.py)
```

---

## Database Model

### Fact Table

* fact_claims

### Dimension Tables

* dim_department
* dim_payer
* dim_provider

---

## Analytical Reports

### Executive Reporting

* Executive Summary
* Top Revenue Cycle Drivers

### Denial Management

* Denial by Department
* Denial Rate Trend Analysis

### Finance & Collections

* AR Aging Analysis
* Payment Variance Analysis
* Payment Speed Trend Analysis

### Financial Reporting

* Monthly Close Reporting
* Month-over-Month Variance Analysis

### Operations

* Department KPI Monitoring
* Department Performance Trends

---

## Statistical Analysis

* Chi-Square Test
* Independent Two-Sample T-Test
* One-Way ANOVA

---

## Automated Deliverables

The pipeline automatically generates a multi-sheet Excel workbook:

* Executive Summary
* Denial RCA
* AR & Collections
* Monthly Close
* Department Performance

---

## Project Structure

```text
Healthcare_RCA/

├── data/
├── output/ (auto created)
├── queries/
├── reports/
├── scripts/

├── build_workbook.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python main.py
```

---

## Skills Demonstrated

* Healthcare Revenue Cycle Analytics
* ETL Development
* SQL Query Development
* PostgreSQL Database Management
* Statistical Hypothesis Testing
* Excel Automation
* Business Reporting
* Data Modeling
* Python Project Architecture
* Analytics Pipeline Development
<img width="1318" height="661" alt="image" src="https://github.com/user-attachments/assets/ed275fd6-6f87-4cf6-ad0e-c5c470db8dee" />
