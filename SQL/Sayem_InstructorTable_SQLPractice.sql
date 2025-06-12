-- Sayem_InstructorTable_SQLPractice.sql
-- Author: Mohammad Sayem Chowdhury
-- Date: 2025-06-12
-- Description: Practice script for creating, modifying, and querying an INSTRUCTOR table. Demonstrates basic SQL DDL and DML operations with clear, personal comments.

-- 0. Drop table INSTRUCTOR if it already exists
DROP TABLE IF EXISTS INSTRUCTOR;

-- 1. Create the INSTRUCTOR table
CREATE TABLE INSTRUCTOR (
    ins_id INTEGER PRIMARY KEY NOT NULL,
    lastname VARCHAR(15) NOT NULL,
    firstname VARCHAR(15) NOT NULL,
    city VARCHAR(15),
    country CHAR(2)
);

-- 2A. Insert a single row for Sayem (personalized)
INSERT INTO INSTRUCTOR (ins_id, lastname, firstname, city, country)
VALUES (1, 'Chowdhury', 'Sayem', 'Toronto', 'CA');

-- 2B. Insert two more rows for demonstration
INSERT INTO INSTRUCTOR (ins_id, lastname, firstname, city, country) VALUES
    (2, 'Chong', 'Raul', 'Toronto', 'CA'),
    (3, 'Vasudevan', 'Hima', 'Chicago', 'US');

-- 3. Select all rows in the table
SELECT * FROM INSTRUCTOR;

-- 3b. Select firstname, lastname, and country where city is Toronto
SELECT firstname, lastname, country FROM INSTRUCTOR WHERE city = 'Toronto';

-- 4. Change the city for Sayem to Markham
UPDATE INSTRUCTOR SET city = 'Markham' WHERE ins_id = 1;

-- 5. Delete the row for Raul Chong
DELETE FROM INSTRUCTOR WHERE ins_id = 2;

-- 5b. Retrieve all rows from the table to see the final state
SELECT * FROM INSTRUCTOR;

-- End of script
