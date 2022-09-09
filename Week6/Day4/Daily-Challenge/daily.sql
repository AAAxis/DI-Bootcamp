-- create table users(
-- id serial primary key, 
-- name varchar(100) not null
-- );

-- create table product_orders (
-- id serial primary key,
-- order_date date not null,
-- user_id int not null,
-- foreign key (user_id) references users
-- );

-- create table items (
-- id serial primary key,
-- name varchar (200),
-- price float not null,
-- order_id int,
-- foreign key (order_id) references product_orders (id)
-- );

-- insert into users 
-- values
-- (default, 'Harry'),
-- (default, 'Ron'),
-- (default, 'Hermione'),
-- (default, 'Luna'),
-- (default, 'Neville');

-- insert into product_orders 
-- values
-- (default, 
-- '2001/08/28', 
-- (select id from users where name = 'Harry')
-- ),

-- (default, 
-- '2001/06/05', 
-- (select id from users where name = 'Hermione')
-- ),

-- (default, 
-- '2001/08/12', 
-- (select id from users where name = 'Ron')
-- ),
 
--  (default, 
-- '2001/08/13', 
-- (select id from users where name = 'Ron')
-- ),

--  (default, 
-- '2001/08/11', 
-- (select id from users where name = 'Neville')
-- ),

--  (default, 
-- '2001/08/28', 
-- (select id from users where name = 'Luna')
-- ),

--  (default, 
-- '2001/09/01', 
-- (select id from users where name = 'Luna')
--  );


-- insert into items 
-- values

-- (default, 
-- 'Phoenix feather Wand',
-- 700,
-- 4
-- ),

-- (default, 
-- 'Dragon Heartstring Wand',
-- 800,
-- 5
-- ),

-- (default, 
-- 'Unicorn Hair Wand',
-- 450,
-- 6
-- ),

-- (default, 
-- 'Unicorn Hair Wand',
-- 450,
-- 7
-- ),

-- (default, 
-- 'Unicorn Hair Wand',
-- 700,
-- 8
-- ),

-- (default, 
-- 'Mysterious Wand',
-- 500,
-- 9
-- ),

-- (default, 
-- 'Oak Wand',
-- 550,
-- 10
-- );

-- CREATE or REPLACE FUNCTION total_price(ui int) 
-- RETURNS float AS $$
-- declare
-- total_sum float;
-- BEGIN
--     total_sum := (select  sum(price) from (select i.name, i.price, po.id
--     from items as i 
--     inner join
--     (select * from product_orders where user_id = ui) as po
--     on i.order_id = po.id) as t
--     order by sum(price))
--     ;
--     RETURN total_sum;  
-- END;
-- $$ LANGUAGE plpgsql;

-- select * from total_price(2);




