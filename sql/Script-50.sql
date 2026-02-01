select title,price,max(price) over() as max_price,MAX(PRICE) over() - price as different
from PRODUCTS
order by title ASC; 
