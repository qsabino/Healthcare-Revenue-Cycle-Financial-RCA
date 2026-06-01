-- BQ: Which payer is costing us the most money?

SELECT
    
    insurance_payer,
    
    ROUND(
        SUM(payment_variance)::NUMERIC,
        2
    ) AS revenue_leakage

FROM fact_claims

GROUP BY insurance_payer

ORDER BY revenue_leakage DESC;