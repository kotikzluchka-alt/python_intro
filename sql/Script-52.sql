create table categories(

id serial PRIMARY key,
title varchar(100),
parent_id serial

);

alter table CATEGORIES alter column parent_id drop not null;

insert into categories(id,title,PARENT_ID ) values
(1,'Электроника',NULL),
(2,'Смартфоны',1),
(3,'Iphone',2),
(4,'Ноутбуки',1);
with recursive r as(
select id,title,1 as level
from categories
where parent_id is NULL

union ALL 

select c.id,c.title, r.level + 1
from categories c
join r on c.parent_id = r.id
)
SELECT *
from r;
