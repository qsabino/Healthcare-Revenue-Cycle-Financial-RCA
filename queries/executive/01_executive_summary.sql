WITH monthly_metrics AS (
    SELECT
        DATE_TRUNC('month', service_date::DATE)::DATE AS month,
        COUNT(*) AS total_claims,
        SUM(claim_amount) AS total_billed,
        SUM(paid_amount)::NUMERIC AS total_paid,
        SUM(payment_variance)::NUMERIC AS revenue_leakage,
        AVG(days_to_payment)::NUMERIC AS avg_days_to_payment,
        AVG(reimbursement_ratio) * 100 AS reimbursement_pct,
        AVG(denial_flag) * 100 AS denial_rate_pct
    FROM fact_claims
    GROUP BY 1
)
SELECT
    month,
    total_claims,
    LAG(total_claims) OVER (ORDER BY month) AS prior_claims,
    total_paid,
    LAG(total_paid) OVER (ORDER BY month) AS prior_paid,
    revenue_leakage,
    LAG(revenue_leakage) OVER (ORDER BY month) AS prior_leakage,
    ROUND(denial_rate_pct,2) AS denial_rate_pct,
    LAG(denial_rate_pct) OVER (ORDER BY month) AS prior_denial_rate,
    ROUND(avg_days_to_payment,2) AS avg_days_to_payment,
    LAG(avg_days_to_payment) OVER (ORDER BY month) AS prior_avg_days
FROM monthly_metrics
ORDER BY month;