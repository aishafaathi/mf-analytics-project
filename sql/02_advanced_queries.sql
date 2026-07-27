
-- 1. Join Fund Master with Performance
SELECT
    fm.scheme_name,
    fm.fund_house,
    fm.category,
    fm.risk_category,
    sp.return_5yr_pct,
    sp.sharpe_ratio,
    sp.aum_crore
FROM fund_master fm
JOIN scheme_performance sp
ON fm.amfi_code = sp.amfi_code
ORDER BY sp.return_5yr_pct DESC;

-- 2. Category-wise Performance
SELECT
    fm.category,
    COUNT(*) AS total_schemes,
    ROUND(AVG(sp.return_5yr_pct),2) AS avg_5yr_return,
    ROUND(AVG(sp.expense_ratio_pct),2) AS avg_expense_ratio
FROM fund_master fm
JOIN scheme_performance sp
ON fm.amfi_code = sp.amfi_code
GROUP BY fm.category
ORDER BY avg_5yr_return DESC;

-- 3. Risk Category vs Average Return
SELECT
    fm.risk_category,
    COUNT(*) AS total_schemes,
    ROUND(AVG(sp.return_5yr_pct),2) AS avg_return
FROM fund_master fm
JOIN scheme_performance sp
ON fm.amfi_code = sp.amfi_code
GROUP BY fm.risk_category
ORDER BY avg_return DESC;

-- 4. Top Fund Houses by Total AUM
SELECT
    fund_house,
    ROUND(SUM(aum_crore),2) AS total_aum
FROM scheme_performance
GROUP BY fund_house
ORDER BY total_aum DESC;

-- 5. Top Rated Funds
SELECT
    scheme_name,
    fund_house,
    morningstar_rating,
    return_5yr_pct
FROM scheme_performance
WHERE morningstar_rating = 5
ORDER BY return_5yr_pct DESC;

-- 6. Top 5 Sharpe Ratio Funds
SELECT
    scheme_name,
    sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 7. Average Return by Fund House
SELECT
    fund_house,
    ROUND(AVG(return_5yr_pct),2) AS avg_return
FROM scheme_performance
GROUP BY fund_house
ORDER BY avg_return DESC;

-- 8. Average AUM by Category
SELECT
    fm.category,
    ROUND(AVG(sp.aum_crore),2) AS average_aum
FROM fund_master fm
JOIN scheme_performance sp
ON fm.amfi_code = sp.amfi_code
GROUP BY fm.category;

-- 9. Highest Expense Ratio Funds
SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
ORDER BY expense_ratio_pct DESC
LIMIT 10;

-- 10. Rank Funds by 5-Year Return
SELECT
    scheme_name,
    return_5yr_pct,
    RANK() OVER (ORDER BY return_5yr_pct DESC) AS rank_position
FROM scheme_performance;