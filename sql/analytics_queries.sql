SELECT
category,
SUM(quantity * price)
AS revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY category
ORDER BY revenue DESC;


SELECT
product_name,
SUM(quantity)
AS total_sold
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY product_name
ORDER BY total_sold DESC
LIMIT 10;

SELECT
AVG(order_value)
FROM orders;

SELECT
customer_id,
COUNT(*)
AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1;


SELECT
city,
SUM(order_value)
AS revenue
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
GROUP BY city
ORDER BY revenue DESC;