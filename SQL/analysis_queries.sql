USE ecommerce;
USE ecommerce;
-- total orders
select count(*) as Total_orders from orders;
-- total sales
SELECT SUM(Net_Amount) AS Total_Sales FROM orders;
-- top product
SELECT Product , SUM(Net_Amount) AS sales FROM orders 
GROUP BY Product
order BY sales DESC;
-- top cities
SELECT city, SUM(Net_Amount) AS sales
FROM orders
GROUP BY city
ORDER BY sales DESC;
-- month sales
SELECT Month , SUM(Net_Amount) AS sales
FROM orders
GROUP BY MONTH;
-- highest profit product
SELECT Product, SUM(Profit) AS Total_Profit
FROM orders
GROUP BY Product
ORDER BY Total_Profit DESC;
-- payment mode distribution
SELECT Payment_Mode, COUNT(*) AS total_orders
FROM orders
GROUP BY Payment_Mode;
-- canceled orders
SELECT *
FROM orders
WHERE Order_Status = 'Cancelled';