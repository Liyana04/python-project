-- USE sql_store;
-- need to put ; for different query 

-- SELECT *
-- FROM customers
-- WHERE customer_id = 1
-- ORDER BY first_name

-- SELECT 
-- 	first_name, 
-- 	last_name, 
-- 	points, 
-- 	(points * 10) + 100 AS discount_factor
-- FROM customers

-- select distinct state
-- from customers

-- SELECT 
-- 	name,
--     unit_price, 
--     unit_price *1.1 AS new_price
-- FROM products

-- SELECT *
-- FROM customers
-- -- WHERE points>3000
-- -- WHERE state != 'VA'
-- WHERE birth_date > '1990-01-01'

-- SELECT *
-- FROM customers
-- WHERE birth_date > '1990-01-01' OR points>1000 AND state ='VA'
-- WHERE birth_date <= '1990-01-01' AND points <= 1000

-- SELECT *
-- FROM order_items
-- WHERE order_id = 6 AND unit_price * quantity >30


-- SELECT *
-- FROM customers
-- -- WHERE state = 'VA' OR state = 'GA' or state = 'FL'
-- -- WHERE state IN ('VA','FL','GA')
-- WHERE state NOT IN ('VA','FL','GA')

-- SELECT *
-- FROM products
-- WHERE quantity_in_stock IN (49,38,72)

-- SELECT *
-- FROM customers
-- -- WHERE points >= 1000 AND points <= 3000
-- WHERE points BETWEEN 1000 AND 3000

-- SELECT *
-- FROM customers
-- WHERE birth_date BETWEEN '1990-01-01' AND '2000-01-01'

-- SELECT *
-- FROM customers
-- WHERE last_name LIKE 'b%'
-- -- will return any customers last_name start with 'b'
-- WHERE last_name LIKE '%b%'
-- -- will return any customers last_name before and after 'b'
-- -- % any number of character
-- -- __single character


-- SELECT *
-- FROM customers
-- -- WHERE phone LIKE '%9'
-- -- WHERE address LIKE '%trail%' OR 
-- 	  -- address LIKE '%AVENUE%' 

-- SELECT *
-- FROM customers
-- WHERE last_name LIKE '%field%'
-- -- WHERE below and above are the same
-- WHERE last_name REGEXP 'field'
-- WHERE last_name REGEXP 'field|mac|rose'
-- -- | means OR ^ measn begining of the string $ is end of the string
-- WHERE last_name REGEXP '[gim]e'
-- --this includes ge, ie, me
-- WHERE last_name REGEXP '[a-h]e'
-- this return name between[a-h] + e
-- ^ beginning of the string
-- $ end
-- | or logical
-- [abcd] match any single character in the bracjet
-- [a-h] range

-- SELECT *
-- FROM customers
-- -- first name are ELKA OR AMBUR
-- WHERE first_name REGEXP 'elka|ambur'
-- -- last name ends with EY or ON
-- where last_name REGEXP 'ey$|on$'
-- -- last name start with MY or SE
-- where last_name REGEXP '^my|se'
-- -- last name contain B followed by R or U
-- where last_name REGEXP 'b[ru]' 
-- -- or can use 'br|bu'

-- null value
-- SELECT *
-- FROM customers
-- WHERE phone IS NULL

-- ORDER BY CALUSE OR SORT
-- SELECT *
-- FROM customers
-- ORDER BY STATE, first_name 

-- SELECT first_name, last_name, 10 AS points
-- FROM customers
-- ORDER BY first_name

-- SELECT *, quantity * unit_price AS total_price
-- FROM order_items
-- WHERE order_id = 2
-- ORDER BY product_id DESC


-- the limit clause
-- SELECT *
-- FROM customers
-- LIMIT 6,3
-- page1: 1-3
-- page2: 4-6
-- page3: 7-9

-- SELECT *
-- FROM customers
-- ORDER BY points DESC
-- LIMIT 3

-- SELECT order_id, orders.customer_id, first_name, last_name
-- FROM orders
-- -- can also use FROM order o, then can use o.customer_id
-- JOIN customers ON orders.customer_id = customers.customer_id
-- -- can also use JOIN customers c, then c.customer_id


-- joining accross database
SELECT *
FROM order_items oi
JOIN sql_inventory.products p
ON oi.product_id = p.product_id
-- if want to use USE sql_inventory also can, then add SELECT *, FROM sql_store.order_items oi

USE sql_hr

select 
	e.employee_id,
    e.first_name,
    e,last_name AS manager
FROM employees e
-- join with it self
JOIN employees m
	ON e.reports_to = m.employee_id
    
-- join 3 tables
USE sql_store;

SELECT 
	o.order_id,
    o.order_date,
    c.first_name,
    c.last_name,
    os.name AS status
FROM orders o
JOIN customers c
	ON o.customer_id = c.customer_id
JOIN order_statuses os
	ON o.status = os.order_status_id
    
-- find the client then find the payment method
USE sql_invoicing;

SELECT 
	p.date,
	p.invoice_date,
	p.amount,
	c.name,
	pm.name
FROM payments p
JOIN clients c
	ON p.client_id = c.client_id
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method


-- compound join condition or multiple join condition
SELECT *
FROM order_items oi
JOIN order_item_notes oin
	ON oi.order_id = oin.order_id
    AND oi.product_id = oin.product_id
    
-- implicit join syntax
SELECT *
FROM orders 0, customers c
WHERE o.customer_id = c.customer_id
-- better use JOIN syntax


-- inner join and outer join
SELECT
	c.customer_id,
    c.first_name,
    o.order_id
FROM customers c
LEFT JOIN orders o
	ON c.customer_id = o.customer_id
ORDER BY c.customer_id
-- left/right join literally means just for comparison, it will return the 'FROM customers c' wether the condition true or not
-- left/right outer join (all things without even match), inner join(all things that match only)
-- have left ad right join, left join will follow based on customers table, right join will follow based on orders table

-- FROM orders o
-- RIGHT JOIN customers c 
-- swap this will follow based on customer table first
-- left/right outer join just same as left/right join


-- outer join from other table
SELECT
	c.customer_id,
    c.first_name,
    o.order_id
    sh.name AS shipper
FROM customers c
LEFT JOIN orders o
	ON c.customer_id = o.customer_id
LEFT JOIN shippers sh
	ON o.shipper_id = sh.shipper_id
ORDER BY c.customer_id


-- 'USING' clause query
SELECT
    o.order_id，
    c.first_name，
    sh.name AS shipper
FROM orders o
JOIN customers c
	-- ON o.customer_id = c.customer_id
    -- same as above
    USING (customer_id)
LEFT JOIN shippers sh
	USING (shipper_id)
    
-- ANOTHER EXAMPLE OF 'USING'
SELECT *
FROM order_items oi
JOIN order_item_notes oin
	-- ON oi.order_id = oin.order_id AND oi.product_id = oin.product_id
    -- same as above
    USING (order_id, product_id)
    
-- natural joins can produce unexpected result, not encourage to use
SELECT 
	o.order_id,
    c.first_name
FROM orders o
NATURAL JOIN customers c


-- cross joins only suitable for small data or table
SELECT 
	c.first_name AS customer,
    p.name AS product
FROM customers c
CROSS JOIN products p
ORDER BY c.first_name

-- implicit syntax (combination of all column from shipper and products into a table)
SELECT 
	sh.name AS shipper,
    p.name AS product
FROM shippers sh, products p
ORDER BY sh.name
-- explicit syntax using cross join
SELECT 
	sh.name AS shipper,
    p.name AS product
FROM shippers sh
CROSS JOIN products p
ORDER BY sh.name


-- unions(combine rows from multiple tables), Whatever in the first query in SELECT determine the column name
SELECT 
	order_id,
    order_date,
    'Active' AS status
FROM orders
WHERE order_date >= '2019-01-01'
UNION
SELECT 
	order_id,
    order_date,
    'Archived' AS status
FROM orders
WHERE order_date < '2019-01-01'

-- less than 2000 is bronze, more than 2000 is silver
SELECT customer_id, first_name, points, 'Bronze' AS Type
FROM customers 
WHERE points< 2000
UNION
SELECT customer_id, first_name, points, 'Silver' AS Type
FROM customers 
WHERE points BETWEEN 2000 AND 3000
UNION
SELECT customer_id, first_name, points, 'Gold' AS Type
FROM customers 
WHERE points > 3000
ORDER BY first_name

-- INSERT INTO ROWS
INSERT INTO customers (
	first_name,
    last_name,
    birth_date,
    address,
    city,
    state
    )
VALUES(
    'John',
    'Smith',
    '2002-01-11',
    'Ampang',
    'Selangor',
    'KL')
    
-- insert multiple rows
INSERT INTO shippers (name)
VALUES ('Shipper1'),
	('Shipper2'),
    ('Shipper3')
    
INSERT INTO products (name, quantity_in_stock, unit_price)
VALUES ('Product 1', 10, 1.95),
	('Beef Wellington', 10, 55.95),
    ('Bag', 20, 11.21)
    
    
-- inserting heirarchical rows
INSERT INTO orders (customer_id, order_date, status)
VALUES (1, '2024-01-02', 1);

INSERT INTO order_items
Values 
	(LAST_INSERT_ID(), 1,1,2.43),
    (LAST_INSERT_ID(), 2,21,21.43)
    
    
-- creating copy table
CREATE TABLE orders_archived AS 
SELECT * FROM orders

-- craeting copy table with conditions
INSERT INTO orders_archived
SELECT *
FROM orders
WHERE order_date < '2019-01-01'

 -- EXERCISE copy table
USE sql_invoicing;

CREATE TABLE invoices_archived AS
SELECT 
	i.invoice_id,
    i.number,
    c.name AS client,
    i.invoice_total,
    i.payment_total,
    i.invoice_date,
    i.payment_date,
    i.due_date    
FROM invoices i
JOIN clients c
	USING (client_id)
WHERE payment_date IS NOT NULL

-- updating a single rows
UPDATE invoices
SET payment_total = 10, payment_date = '2025-01-01'
WHERE invoice_id = 1

UPDATE invoices
SET payment_total = invoice_total * 0.5, payment_date = due_date
WHERE invoice_id = 3

-- updating multiple rows
UPDATE invoices
SET payment_total = invoice_total * 0.5, payment_date = due_date
WHERE client_id IN (3,4)

-- exercise updating multiple rows
USE sql_store;

UPDATE customers
SET points = points + 50
WHERE birth_date < '1990-01-01'

-- using subqueries in update run the select query first before updating
UPDATE invoices
SET payment_total = invoice_total * 0.5, payment_date = due_date
WHERE invoice_id IN 
	(SELECT client_id
	FROM clients
	WHERE name = 'MyWorks')
-- can also use WHERE state IN ('CA','NY')


-- exercise
UPDATE orders
SET customers = 'Gold customer'
WHERE customer_id IN
				(SELECT customer_id
				FROM customers
				WHERE points>3000)
                
-- delete rows
DELETE FROM invoices
WHERE invoice_id (
				SELECT *
				FROM clients
				WHERE name = "My Works")
                
                
-- restoring db ust rerun sql query


