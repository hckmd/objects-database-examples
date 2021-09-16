cursor.execute('SELECT * FROM student')
rows = cursor.fetchall()

students = []
for row in rows:
    student = Student (
        name = row[0],
        english_mark = row[1],
        maths_mark = row[2]
    )
    students.append(student)