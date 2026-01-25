select name,(PRICE * QUANTITY ) as cheque
from USERS
join ORDERS on users.ID = USER_ID
join ORDERITEMS on orders.ID = ORDER_ID 
join PRODUCTS on  ORDERITEMS.PRODUCT_ID = PRODUCTS.ID
where name = 'Вася';

select name
from USERS 
join ORDERS on users.ID = USER_ID
left join ORDERITEMS on orders.ID = ORDER_ID 
where PRODUCT_ID is null;