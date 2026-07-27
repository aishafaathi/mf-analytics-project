-- ==================================================
-- DASHBOARD QUERIES
-- ==================================================

-- Dashboard Dataset
SELECT * FROM dashboard_dataset;

-- Top Performing Funds
SELECT
    scheme_name,
    return_5yr_pct
FROM dashboard_dataset
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- AUM by Fund House
SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM dashboard_dataset
GROUP BY fund_house
ORDER BY total_aum DESC;

-- Risk Distribution
SELECT
    risk_category,
    COUNT(*) AS total_funds
FROM dashboard_dataset
GROUP BY risk_category;

-- Morningstar Rating Distribution
SELECT
    morningstar_rating,
    COUNT(*) AS total_funds
FROM dashboard_dataset
GROUP BY morningstar_rating;
