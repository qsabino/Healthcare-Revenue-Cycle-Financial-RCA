-- BQ: Are reimbursements becoming slower over time?

WITH monthly_payment_speed AS (
    SELECT
        DATE_TRUNC('month', service_date::DATE)::DATE AS month,
        AVG(days_to_payment):: NUMERIC AS avg_days
    FROM fact_claims
    GROUP BY 1
)
SELECT  
    month,
    ROUND(avg_days,2) AS avg_days,
    LAG(avg_days) OVER (ORDER BY month) AS prior_month,
    (avg_days - LAG(avg_days) OVER (ORDER BY month)) AS variance
FROM monthly_payment_speed
ORDER BY month;