class Student:
    def __init__(self, id: int, name: str, english_mark: int, maths_mark: int):
        self.id = id
        self.name = name
        self.english_mark = english_mark
        self.maths_mark = maths_mark

import sqlite3 
# Opens connection with records.db file, assuming it already exists
connection = sqlite3.connect('records.db') 
cursor = connection.cursor()

# Retrieve all the student records from the database
cursor.execute('SELECT * FROM student')
rows = cursor.fetchall()

# Go through each record and map to Student objects
students = []
for row in rows:
    student = Student (
        id = row[0],
        name = row[1],
        english_mark = row[2],
        maths_mark = row[3]
    )
    students.append(student)

# Print out each student object in our list
for student in students:
    print()
    print(f'Name: { student.name }')
    print(f'Student ID: { student.id }')
    print(f'English mark: { student.english_mark }')
    print(f'Maths mark: { student.maths_mark }')