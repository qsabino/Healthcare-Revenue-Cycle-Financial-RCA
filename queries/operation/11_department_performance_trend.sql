-- BQ: Which departments are getting worse in revenue leakage over time?


WITH dept_month AS (

    SELECT
        
		department,
        
		DATE_TRUNC('month', service_date::DATE)::DATE AS month,
        
		SUM(payment_variance)::NUMERIC AS leakage

    FROM fact_claims

    GROUP BY 1,2

)

SELECT
    
	department,
    
	month,
    
	leakage,

    ROUND(
		LAG(leakage) OVER (
        	PARTITION BY department
        	ORDER BY month
    	), 
		2) AS prior_month,

	ROUND(
	    leakage
	        - LAG(leakage) OVER (
	            PARTITION BY department
	            ORDER BY month
	        ),
		2) AS change_amount

FROM dept_month;