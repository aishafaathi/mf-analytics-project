SELECT
    scheme_name,
    fund_house,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

SELECT
    fund_house,
    ROUND(AVG(expense_ratio_pct), 2) AS avg_expense_ratio
FROM scheme_performance
GROUP BY fund_house
ORDER BY avg_expense_ratio DESC;

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 10;

SELECT
    morningstar_rating,
    COUNT(*) AS total_schemes
FROM scheme_performance
GROUP BY morningstar_rating
ORDER BY morningstar_rating;

SELECT
    fund_house,
    COUNT(*) AS schemes
FROM fund_master
GROUP BY fund_house
ORDER BY schemes DESC;
