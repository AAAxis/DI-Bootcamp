-- insert into book ( title, author)
-- values
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To kill a mockingbird', 'Harper Lee');

-- create table student 
-- (student_id SERIAL PRIMARY KEY, 
--  name varchar (50) not null unique, 
--  age int check (age between 0 and 15)

-- insert into student (name, age)
-- values
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);

-- create table my_library 
-- (book_fk_id int, 
--  student_fk_id int, 
--  borrowed_date date,
 
--  primary key (book_fk_id, student_fk_id),
--  foreign key (book_fk_id) references book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
--  foreign key (student_fk_id) references student (student_id) ON DELETE CASCADE ON UPDATE CASCADE
--  );


-- Add 4 records in the junction table, use subqueries.
-- the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
-- the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
-- the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
-- the student named Bob, borrowed the book Harry Potter the on 12/08/2021

-- insert into my_library (book_fk_id, student_fk_id, borrowed_date)
-- values
-- (
--      (select book_id from book where title = 'Harry Potter'),
--      (select student_id from student where name = 'Bob'),'2021/08/12'
-- );

-- Select all the columns from the junction table
-- select * from my_library;
-- Select the name of the student and the title of the borrowed books

-- select s.name, b.title, m.borrowed_date
-- from student as s
-- inner join my_library as m 
-- on s.student_id = m.student_fk_id 
-- inner join book as b 
-- on b.book_id = m.book_fk_id;

-- Select the average age of the children, that borrowed the book Alice in Wonderland



-- select avg(age) from student 
-- where id in (select student_id from my_library where book_fk_id) = 
-- (select book_id from book where title = 'Alice in Wonderland');


-- Delete a student from the Student table, what happened in the junction table ?
-- delete from student where student_id in (1,2)

-- select * from my_library