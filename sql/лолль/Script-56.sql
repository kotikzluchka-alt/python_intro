select sum(amount) as total_amount
from ORDERS O;

refresh materialized view view1;

select *
from view1;