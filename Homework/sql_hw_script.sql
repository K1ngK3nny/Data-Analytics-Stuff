USE sakila;
SELECT 
    first_name, last_name
FROM
    actor;

SELECT 
    CONCAT(UPPER(first_name), ' ', UPPER(last_name)) AS Actor_Name
FROM
    actor;

SELECT 
    actor_id, first_name, Last_name
FROM
    actor
WHERE
    first_name = 'Joe';

SELECT 
    first_name, last_name
FROM
    actor
WHERE
    last_name LIKE '%gen%';

SELECT 
    CONCAT(last_name, ' ', first_name)
FROM
    actor
WHERE
    last_name LIKE '%li%';

SELECT 
    country_id, country
FROM
    country
WHERE
    country IN ('Afghanistan' , 'Bangladesh', 'China');

ALTER TABLE actor
MODIFY COLUMN middle_name blob
AFTER first_name;

ALTER TABLE actor
DROP COLUMN middle_name;

SELECT 
    COUNT(last_name), last_name
FROM
    actor
GROUP BY last_name
HAVING COUNT(last_name) >= 2;

UPDATE actor 
SET 
    first_name = 'Harpo'
WHERE
    last_name = 'Williams'
        AND first_name = 'Groucho';

UPDATE actor 
SET 
    first_name = 'Mucho Groucho'
WHERE
    last_name = 'Williams'
        AND first_name = 'Harpo';
        
-- to re create schema for address table        
/* CREATE TABLE address (
        smallint(5) UN AI PK 
        address varchar(50) 
        address2 varchar(50) 
        district varchar(20) 
        city_id smallint(5) UN 
        postal_code varchar(10) 
        phone varchar(20) 
        location geometry 
        last_update timestamp
        )*/

SELECT first_name, last_name, address.address
FROM staff 
INNER JOIN address
ON staff.address_id=address.address_id;

select sum(amount)
from payment
INNER JOIN staff
ON staff.staff_id=payment.staff_id;

SELECT actor_id, film_id
FROM film_actor
INNER JOIN film ON film.film_id = film_actor.film_id;

select count("Hunchback Impossible")
from inventory;

select title
from film
group by rental_rate DESC;






