-- ==========================================================
-- Digital Nurture 5.0
-- Module 3 - Database Integration
-- Hands-On 4
-- Task 1 : Baseline Performance (No Indexes)
-- ==========================================================

USE college_db;

-- Display the execution plan for the query.

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

-- Observation
/*
Since no indexes are created yet,
students and enrollments may use
table scans.
*/

-- Document your findings.

/*

Sample Observation

Possible Access Type:
ALL (Full Table Scan)

Rows Examined:
Depends on your data.

Join Type:
Nested Loop

Conclusion:

Since no additional indexes exist,
MySQL scans the tables to locate
matching records.

Performance is acceptable for
small datasets but inefficient
for large databases.

*/