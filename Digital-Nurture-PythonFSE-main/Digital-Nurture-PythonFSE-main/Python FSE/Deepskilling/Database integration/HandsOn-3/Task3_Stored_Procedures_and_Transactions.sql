-- ==========================================================
-- Digital Nurture 5.0
-- Module 3 - Database Integration
-- Hands-On 3
-- Task 3 : Stored Procedures and Transactions
-- ==========================================================

USE college_db;

-- Create Stored Procedure to Enroll a Student

DROP PROCEDURE IF EXISTS sp_enroll_student;

DELIMITER $$

CREATE PROCEDURE sp_enroll_student(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)

BEGIN

    IF EXISTS(
        SELECT 1
        FROM enrollments
        WHERE student_id = p_student_id
        AND course_id = p_course_id
    )

    THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT='Student is already enrolled in this course';

    ELSE

        INSERT INTO enrollments
        (
            student_id,
            course_id,
            enrollment_date,
            grade
        )

        VALUES
        (
            p_student_id,
            p_course_id,
            p_enrollment_date,
            NULL
        );

    END IF;

END $$

DELIMITER ;

-- Test Stored Procedure

CALL sp_enroll_student(10,2,'2024-01-15');


-- Create Department Transfer Log Table


CREATE TABLE IF NOT EXISTS department_transfer_log
(
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    old_department INT,
    new_department INT,
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Stored Procedure for Department Transfer

DROP PROCEDURE IF EXISTS sp_transfer_student;

DELIMITER $$

CREATE PROCEDURE sp_transfer_student
(
    IN p_student_id INT,
    IN p_new_department INT
)

BEGIN

    DECLARE v_old_department INT;

    START TRANSACTION;

    SELECT department_id
    INTO v_old_department
    FROM students
    WHERE student_id = p_student_id;

    UPDATE students
    SET department_id = p_new_department
    WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log
    (
        student_id,
        old_department,
        new_department
    )

    VALUES
    (
        p_student_id,
        v_old_department,
        p_new_department
    );

    COMMIT;

END $$

DELIMITER ;

-- Test Department Transfer

CALL sp_transfer_student(2,3);

SELECT *
FROM department_transfer_log;

-- Demonstrate Rollback

START TRANSACTION;

UPDATE students
SET department_id=2
WHERE student_id=1;

-- Intentional Error
INSERT INTO department_transfer_log
(student_id,old_department,new_department)
VALUES
(NULL,NULL,NULL);

ROLLBACK;

SELECT *
FROM students
WHERE student_id=1;


-- SAVEPOINT Example

START TRANSACTION;

INSERT INTO enrollments
(student_id,course_id,enrollment_date,grade)
VALUES
(9,2,CURDATE(),NULL);

SAVEPOINT first_insert;

-- Intentional Duplicate Insert
INSERT INTO enrollments
(student_id,course_id,enrollment_date,grade)
VALUES
(9,2,CURDATE(),NULL);

ROLLBACK TO first_insert;

COMMIT;

-- Verify

SELECT *
FROM enrollments
WHERE student_id=9;

