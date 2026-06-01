-- BQ: Which departments have the highest denial rates?


SELECT
    
    department,
    
    COUNT(*) AS total_claims,
    
    SUM(denial_flag)::NUMERIC AS denied_claims,
    
    ROUND(
        SUM(denial_flag) / COUNT(*) * 100,
        2
    ) AS denial_rate_pct

FROM fact_claims

GROUP BY department

ORDER BY denial_rate_pct DESC;