-- Use SQL to get the following from the database:
-- All items, ordered by price (lowest to highest).
-- select * from items order by price asc

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- select * from items where price > 80 order by price desc

-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
-- select fname, lname from customers order by fname limit 3


-- All last names (no other columns!), in reverse alphabetical order (Z-A)
-- select lname from customers order by fname desc

-- select * from customer

-- select first_name ||' '|| last_name as full_name from customer;

-- select create_date from customer limit 1

-- select* from customer order by first_name desc

-- select film_ID, title, description, release_year, rental_rate from film order by rental_rate;
-- select address, phone from address where district = 'Texas';

-- select * from film where film_id in (15, 150);
-- select film_id, title, description, length, rental_rate from film where title = 'Harry Potter';

-- select film_id, title, description, length, rental_rate
-- from film
-- where title ilike 'ha%';

-- select film_id ,title, rental_rate 
-- from film
-- order by rental_rate limit 10; 

-- select film_id ,title, rental_rate 
-- from film
-- order by rental_rate offset 10; 

-- select film_id ,title, rental_rate 
-- from film
-- order by rental_rate offset 10 limit 10;

-- select c.customer_id, c.first_name ||' '|| c.last_name as full_name, p.payment_date, p.amount
-- from payment as p 
-- inner join customer as c
-- on p.customer_id = c.customer_id
-- order by c.customer_id; 

-- select f.film_id, f.title 
-- from film as f 
-- where f.film_id not in (select film_id from inventory);

-- select city, country from city
-- inner join country 
-- on city.country_id = country.country_id

-- select c.first_name ||' '|| c.last_name as customer_name, s.first_name ||' '|| s.last_name as staff_name
-- from customer as c
-- inner join staff as s
-- on c.store_id = s.store_id;


