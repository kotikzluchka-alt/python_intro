create table users(

id serial primary key,
name Varchar(100),
email varchar(100)

);

create table products(

id serial primary key,
title varchar(100),
price decimal

);

create table orders(

id serial primary key,
user_id integer references users (id),
created_at TIMESTAMP

);

create table orderitems(

id serial primary key,
order_id integer references orders (id),
product_id integer references products (id),
quantity integer

);