-- ==========================================================
-- Digital Nurture 5.0
-- Module 3 - Database Integration
-- Hands-On 3
-- Task 2 : Creating and Using Views
-- ==========================================================

USE college_db;

-- Create a view showing each student's full name, department, number of courses, and GPA.

CREATE OR REPLACE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name,' ',s.last_name) AS student_name,
    d.dept_name,
    COUNT(e.course_id) AS total_courses,

    ROUND(
        AVG(
            CASE
                WHEN e.grade='A' THEN 4
                WHEN e.grade='B' THEN 3
                WHEN e.grade='C' THEN 2
                WHEN e.grade='D' THEN 1
                WHEN e.grade='F' THEN 0
            END
        ),2
    ) AS GPA

FROM students s
LEFT JOIN departments d
ON s.department_id=d.department_id

LEFT JOIN enrollments e
ON s.student_id=e.student_id

GROUP BY
s.student_id,
student_name,
d.dept_name;

-- Create course statistics view.

CREATE OR REPLACE VIEW vw_course_stats AS

SELECT

    c.course_name,
    c.course_code,

    COUNT(e.enrollment_id) AS total_enrollments,

    ROUND(
        AVG(
            CASE
                WHEN e.grade='A' THEN 4
                WHEN e.grade='B' THEN 3
                WHEN e.grade='C' THEN 2
                WHEN e.grade='D' THEN 1
                WHEN e.grade='F' THEN 0
            END
        ),2
    ) AS avg_gpa

FROM courses c

LEFT JOIN enrollments e
ON c.course_id=e.course_id

GROUP BY
c.course_id,
c.course_name,
c.course_code;


-- Display students having GPA greater than 3.


SELECT *
FROM vw_student_enrollment_summary
WHERE GPA > 3;


-- Attempt to update the multi-table view.


UPDATE vw_student_enrollment_summary
SET student_name='Test Student'
WHERE student_id=1;

-- Expected Result:
-- MySQL will generate an error because complex views created using multiple tables, GROUP BY and aggregate functions are not updatable.

-- Drop both views.

DROP VIEW IF EXISTS vw_student_enrollment_summary;

DROP VIEW IF EXISTS vw_course_stats;

-- Create a single-table view using WITH CHECK OPTION.

CREATE OR REPLACE VIEW vw_student_2022 AS

SELECT
student_id,
first_name,
last_name,
email,
enrollment_year

FROM students

WHERE enrollment_year=2022

WITH CHECK OPTION;

-- Verify the View

SELECT *
FROM vw_student_2022;
