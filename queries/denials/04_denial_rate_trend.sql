-- BQ: Are denials improving or worsening over time?


WITH monthly_denials AS (

    SELECT
        
        DATE_TRUNC('month', service_date::DATE)::DATE AS month,
        
        ROUND(
            AVG(denial_flag)::NUMERIC * 100,
            2
        ) AS denial_rate

    FROM fact_claims

    GROUP BY 1

)

SELECT
    
    month,
    
    denial_rate,

    LAG(denial_rate) OVER (
        ORDER BY month
    ) AS prior_denial_rate,

    denial_rate
        - LAG(denial_rate) OVER (
            ORDER BY month
        ) AS denial_rate_change

FROM monthly_denials

ORDER BY month;