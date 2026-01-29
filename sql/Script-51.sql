with prev_orders as (
select id, 
user_id, 
CREATED_AT ,
lag(CREATED_AT ) over(partition by user_id order by created_at asc) as prev_date
from orders)
select *,created_at - prev_date
from prev_orders;
create table categories(

id serial PRIMARY key,
title varchar(100),
parent_id serial

);

insert into categories
(1,'Электроника',NULL),
(2,'Смартфоны',1),
(3,'Iphone',2),
(4,'Ноутбуки',1)
