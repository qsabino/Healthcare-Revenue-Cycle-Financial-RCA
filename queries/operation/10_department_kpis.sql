-- Which departments perform best?

SELECT
    
    department,
    
    COUNT(*) AS claims,
    
    ROUND(
        AVG(claim_amount)::NUMERIC,
        2
    ) AS avg_claim,
    
    ROUND(
        AVG(paid_amount)::NUMERIC,
        2
    ) AS avg_paid,
    
    ROUND(
        AVG(days_to_payment)::NUMERIC,
        2
    ) AS avg_days_to_payment,
    
    ROUND(
        AVG(reimbursement_ratio)::NUMERIC * 100,
        2
    ) AS reimbursement_pct

FROM fact_claims

GROUP BY department

ORDER BY reimbursement_pct DESC;