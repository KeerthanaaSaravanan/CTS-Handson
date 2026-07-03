-- ==========================================================
-- Digital Nurture 5.0
-- Module 3 - Database Integration
-- Hands-On 2
-- Task 4 : Aggregations and Grouping
-- ==========================================================

USE college_db;

-- Calculate the total number of enrollments for each course.

SELECT
    c.course_name,
    COUNT(e.enrollment_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
ORDER BY enrollment_count DESC;

-- Find the average salary of professors in each department.

SELECT
    d.dept_name,
    ROUND(AVG(p.salary), 2) AS average_salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id
GROUP BY d.department_id, d.dept_name;

-- Find departments where total budget exceeds 600000.

SELECT
    dept_name,
    budget
FROM departments
WHERE budget > 600000;

-- Show grade distribution for course CS101.

SELECT
    e.grade,
    COUNT(*) AS total_students
FROM enrollments e
INNER JOIN courses c
ON e.course_id = c.course_id
WHERE c.course_code = 'CS101'
GROUP BY e.grade
ORDER BY e.grade;


-- List departments having more than two enrolled students.

SELECT
    d.dept_name,
    COUNT(DISTINCT s.student_id) AS total_students
FROM departments d
INNER JOIN students s
ON d.department_id = s.department_id
GROUP BY d.department_id, d.dept_name
HAVING COUNT(DISTINCT s.student_id) > 2;

