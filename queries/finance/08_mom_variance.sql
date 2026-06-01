-- BQ: How did collections/revenue change compared to last month?


WITH monthly_summary AS (

    SELECT

        DATE_TRUNC('month', service_date::DATE)::DATE AS month,

        SUM(paid_amount)::NUMERIC AS total_paid

    FROM fact_claims

    GROUP BY 1

)

SELECT

    month,

    total_paid,

    LAG(total_paid) OVER (
        ORDER BY month
    ) AS prior_month_paid,

    total_paid
        - LAG(total_paid) OVER (
            ORDER BY month
        ) AS change_amount,

    ROUND(
        (
            total_paid
            - LAG(total_paid) OVER (
                ORDER BY month
            )
        )
        /
        NULLIF(
            LAG(total_paid) OVER (
                ORDER BY month
            ),
            0
        ) * 100,
        2
    ) AS pct_change

FROM monthly_summary

ORDER BY month;