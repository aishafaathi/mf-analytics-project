-- ============================================
-- CREATE VIEW: PERFORMANCE SUMMARY
-- ============================================

DROP VIEW IF EXISTS performance_summary;

CREATE VIEW performance_summary AS
SELECT
    fm.amfi_code,
    fm.scheme_name,
    fm.fund_house,
    fm.category,
    fm.risk_category,
    sp.return_1yr_pct,
    sp.return_3yr_pct,
    sp.return_5yr_pct,
    sp.sharpe_ratio,
    sp.expense_ratio_pct,
    sp.aum_crore,
    sp.morningstar_rating
FROM fund_master fm
JOIN scheme_performance sp
ON fm.amfi_code = sp.amfi_code;


-- ============================================
-- CREATE VIEW: LATEST NAV
-- ============================================

DROP VIEW IF EXISTS latest_nav;

CREATE VIEW latest_nav AS
SELECT
    n.amfi_code,
    n.date,
    n.nav
FROM nav_history n
JOIN (
    SELECT
        amfi_code,
        MAX(date) AS latest_date
    FROM nav_history
    GROUP BY amfi_code
) latest
ON n.amfi_code = latest.amfi_code
AND n.date = latest.latest_date;


-- ============================================
-- CREATE VIEW: DASHBOARD DATASET
-- ============================================

DROP VIEW IF EXISTS dashboard_dataset;

CREATE VIEW dashboard_dataset AS
SELECT
    ps.scheme_name,
    ps.fund_house,
    ps.category,
    ps.risk_category,
    ps.return_5yr_pct,
    ps.aum_crore,
    ps.expense_ratio_pct,
    ps.morningstar_rating,
    ln.nav AS latest_nav
FROM performance_summary ps
JOIN latest_nav ln
ON ps.amfi_code = ln.amfi_code;