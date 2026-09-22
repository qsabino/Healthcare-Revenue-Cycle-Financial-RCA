-- BQ: How is the performance in each month?

SELECT
    DATE_TRUNC('month', service_date::DATE)::DATE AS month,
    COUNT(*) AS claims,
    ROUND(SUM(claim_amount)::NUMERIC, 2) AS total_billed,
    ROUND(SUM(paid_amount)::NUMERIC, 2) AS total_paid,
    ROUND(SUM(payment_variance)::NUMERIC, 2) AS total_variance
FROM fact_claims
GROUP BY 1
ORDER BY month;