/*
AR = Accounts Receivable, money owed to the healthcare provider that hasn't been collected yet.
BQ: How much money is sitting unpaid?
*/


SELECT
    
    aging_bucket,
    
    COUNT(*) AS claim_count,
    
    ROUND(
        SUM(payment_variance)::NUMERIC,
        2
    ) AS outstanding_ar

FROM fact_claims

GROUP BY aging_bucket

ORDER BY aging_bucket;