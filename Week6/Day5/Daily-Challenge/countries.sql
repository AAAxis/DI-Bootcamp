create table countries 
(enter_id serial primary key,
 name varchar(100) not null,
 capital varchar (100) not null,
 flag bytea, 
 subregion varchar (100), 
 population float not null);