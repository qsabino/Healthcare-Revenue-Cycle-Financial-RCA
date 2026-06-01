-- BQ: What is causing the financial problem?

SELECT

    denial_reason,

    COUNT(*) AS denied_claims,

    SUM(payment_variance) AS leakage

FROM fact_claims

WHERE denial_flag = 1

GROUP BY denial_reason

ORDER BY leakage DESC;