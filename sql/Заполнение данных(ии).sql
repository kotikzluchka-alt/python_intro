TRUNCATE users, products, orders, orderitems RESTART IDENTITY CASCADE;

-- 1. Генерируем 1000 пользователей
INSERT INTO users (name, email)
SELECT 
    'User_' || i, 
    'user_' || i || '@test.com'
FROM generate_series(1, 1000) AS i;

-- 2. Генерируем 100 товаров (со случайной ценой от 10 до 1000)
INSERT INTO products (title, price)
SELECT 
    'Product_' || i, 
    (random() * 1000 + 10)::decimal(10, 2)
FROM generate_series(1, 100) AS i;

-- 3. Генерируем 10 000 заказов
-- (Случайный user_id от 1 до 1000, случайная дата за последний год)
INSERT INTO orders (user_id, created_at)
SELECT 
    floor(random() * 1000 + 1)::int,
    NOW() - (random() * interval '365 days')
FROM generate_series(1, 10000) AS i;

-- 4. Генерируем 50 000 позиций в чеках (OrderItems)
-- (Случайный order_id от 1 до 10000, случайный товар, случайное кол-во 1-5)
INSERT INTO orderitems (order_id, product_id, quantity)
SELECT 
    floor(random() * 10000 + 1)::int,
    floor(random() * 100 + 1)::int,
    floor(random() * 5 + 1)::int
FROM generate_series(1, 50000) AS i;