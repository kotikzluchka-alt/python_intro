--alter table BIG_ORDERS alter column name type integer using name::integer;
--update BIG_ORDERS set count = count + 1 ;
--vacuum full big_orders;
explain analyse
select *
from big_orders;