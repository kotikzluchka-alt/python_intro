drop materialized view view1;

create materialized view view1 as
with recursive data_0 as (
select '2023-10-01'::date as dates,0 as zero
union ALL 
select dates + 1,zero
from data_0
where dates < '2023-10-31'::date 
),
v as (select dates,(coalesce(o.amount,zero)) as total_amount
from data_0 
left join orders o on dates = o.DATE_ORDERS
)
select dates,sum(total_amount)
from v
group by dates
order by dates asc;