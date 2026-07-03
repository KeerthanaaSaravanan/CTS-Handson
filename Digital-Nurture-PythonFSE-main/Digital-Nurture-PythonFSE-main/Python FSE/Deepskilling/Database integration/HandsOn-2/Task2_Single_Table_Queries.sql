-- ==========================================================
-- Digital Nurture 5.0
-- Module 3 - Database Integration
-- Hands-On 2
-- Task 2 : Single Table Queries and Filtering
-- ==========================================================

USE college_db;

-- Retrieve all students enrolled in 2022,ordered by last_name alphabetically.

SELECT *
FROM students
WHERE enrollment_year = 2022
ORDER BY last_name ASC;


-- Find all courses with more than 3 credits,sorted by credits in descending order.


SELECT *
FROM courses
WHERE credits > 3
ORDER BY credits DESC;


-- List all professors whose salary is between 80,000 and 95,000.

SELECT *
FROM professors
WHERE salary BETWEEN 80000 AND 95000;

-- Find all students whose email ends with '@college.edu'.

SELECT *
FROM students
WHERE email LIKE '%@college.edu';

-- Count the total number of students per enrollment year.

SELECT
    enrollment_year,
    COUNT(*) AS total_students
FROM students
GROUP BY enrollment_year
ORDER BY enrollment_year;

