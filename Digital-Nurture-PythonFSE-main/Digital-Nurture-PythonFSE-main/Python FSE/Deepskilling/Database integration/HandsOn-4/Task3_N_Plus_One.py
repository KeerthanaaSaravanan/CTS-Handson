# ==========================================================
# Digital Nurture 5.0
# Module 3 - Database Integration
# Hands-On 4
# Task 3 : N+1 Query Problem
# ==========================================================

import mysql.connector # type: ignore
import time


# Database Connection

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = connection.cursor()

# Version 1 : N+1 Query Problem

print("=" * 60)
print("VERSION 1 : N+1 QUERY")
print("=" * 60)

query_count = 0

start = time.time()

cursor.execute("SELECT * FROM enrollments")
query_count += 1

enrollments = cursor.fetchall()

for enrollment in enrollments:

    student_id = enrollment[1]

    cursor.execute(
        "SELECT first_name, last_name FROM students WHERE student_id=%s",
        (student_id,)
    )

    query_count += 1

    student = cursor.fetchone()

    print(student[0], student[1])

end = time.time()

print("\nQueries Executed :", query_count)
print("Execution Time :", round(end-start,5), "seconds")

# Version 2 : Optimized JOIN Query

print("\n")
print("=" * 60)
print("VERSION 2 : SINGLE JOIN")
print("=" * 60)

start = time.time()

cursor.execute("""
SELECT
    s.first_name,
    s.last_name,
    c.course_name,
    e.grade

FROM enrollments e

JOIN students s
ON e.student_id=s.student_id

JOIN courses c
ON e.course_id=c.course_id
""")

records = cursor.fetchall()

for row in records:

    print(
        row[0],
        row[1],
        "-",
        row[2],
        "- Grade:",
        row[3]
    )

end = time.time()

print("\nQueries Executed : 1")
print("Execution Time :", round(end-start,5), "seconds")


# Close Connection

cursor.close()
connection.close()

print("\nConnection Closed.")