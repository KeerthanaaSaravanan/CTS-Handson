-- ==========================================================
-- Digital Nurture 5.0
-- Module 3 - Database Integration
-- Hands-On 4
-- Task 2 : Add Indexes and Compare Plans
-- ==========================================================

USE college_db;

-- Create a B-Tree Index on enrollment_year

CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);

-- Verify
SHOW INDEX FROM students;

-- Create Composite UNIQUE Index

CREATE UNIQUE INDEX idx_enrollment_student_course
ON enrollments(student_id, course_id);

-- Verify
SHOW INDEX FROM enrollments;

-- Create Index on course_code

CREATE INDEX idx_course_code
ON courses(course_code);

-- Verify
SHOW INDEX FROM courses;

-- Compare Query Plan

EXPLAIN FORMAT=JSON

SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

-- Partial Index

CREATE INDEX idx_grade
ON enrollments(grade);

SHOW INDEX FROM enrollments;

