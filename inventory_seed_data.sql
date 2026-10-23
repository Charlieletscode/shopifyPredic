-- Dummy Data Schema for Predictive Inventory
-- This SQL structure mimics a product sales ledger that could be imported/used by the predictive model.

CREATE TABLE IF NOT EXISTS sales_records (
    sale_id INT PRIMARY KEY,
    product_sku VARCHAR(50) NOT NULL,
    sale_date DATE NOT NULL,
    quantity_sold INT NOT NULL,
    price_at_sale DECIMAL(10, 2) NOT NULL
);

-- Sample Data Insertion (to simulate a real dataset)
INSERT INTO sales_records (sale_id, product_sku, sale_date, quantity_sold, price_at_sale) VALUES
(1, 'SKU-A101', '2026-09-01', 5, 29.99),
(2, 'SKU-B202', '2026-09-01', 12, 199.50),
(3, 'SKU-A101', '2026-09-05', 8, 29.99),
(4, 'SKU-C303', '2026-09-10', 2, 499.00),
(5, 'SKU-B202', '2026-09-12', 15, 199.50),
(6, 'SKU-A101', '2026-09-15', 6, 29.99),
(7, 'SKU-C303', '2026-09-20', 3, 499.00),
(8, 'SKU-B202', '2026-09-22', 10, 199.50),
-- Adding a simulated spike/anomaly to test model robustness
(9, 'SKU-A101', '2026-10-10', 35, 29.99);