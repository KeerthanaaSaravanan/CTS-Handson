-- ==========================================================
-- Digital Nurture 5.0
-- Module 3 - Database Integration
-- Hands-On 3
-- Task 1 : Subqueries
-- ==========================================================

USE college_db;

-- Find students enrolled in more courses than the average number of enrollments per student.

SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    COUNT(e.course_id) AS total_courses
FROM students s
INNER JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(course_id) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) AS avg_enrollment
);

-- List courses where every enrolled student has received grade 'A'.
SELECT
    c.course_id,
    c.course_name
FROM courses c
WHERE NOT EXISTS
(
    SELECT *
    FROM enrollments e
    WHERE e.course_id = c.course_id
    AND (e.grade <> 'A' OR e.grade IS NULL)
);

-- Step 37
-- Find the professor with the highest salary in each department.


SELECT
    p.prof_name,
    d.dept_name,
    p.salary
FROM professors p
INNER JOIN departments d
ON p.department_id = d.department_id
WHERE p.salary =
(
    SELECT MAX(salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);

-- Step 38
-- Find departments where average professor salary exceeds 85000 using a derived table.


SELECT *
FROM
(
    SELECT
        d.dept_name,
        AVG(p.salary) AS average_salary
    FROM departments d
    INNER JOIN professors p
    ON d.department_id = p.department_id
    GROUP BY d.department_id, d.dept_name
) AS department_salary
WHERE average_salary > 85000;

