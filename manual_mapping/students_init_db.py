import sqlite3 
# Opens connection with records.db file, creating if it doesn't exist
connection = sqlite3.connect('records.db') 
cursor = connection.cursor()

# Creates table for student data
cursor.execute("CREATE TABLE student (id INT PRIMARY KEY, name TEXT," +
 "english_mark INT, maths_mark INT)")

# Inserts records for two students
cursor.execute("INSERT INTO student VALUES (1, 'Jim', 80, 80)")
cursor.execute("INSERT INTO student VALUES (2, 'Pam', 85, 85)")

# Commit the changes and close the connection
connection.commit()
connection.close()
