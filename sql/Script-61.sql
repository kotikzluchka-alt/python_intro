insert into big_orders(name,count)
with recursive rec1 as (
select 1 as name,1 as counts
union all
select name + 1,counts
from rec1
where name < 1000000
)
select *
from rec1;

