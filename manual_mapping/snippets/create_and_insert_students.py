cursor.execute("CREATE TABLE student (id INT PRIMARY KEY AUTOINCREMENT, name TEXT," +
 "english_mark INT, maths_mark INT)")

cursor.execute("INSERT INTO student VALUES ('Jim', 80, 80)")
cursor.execute("INSERT INTO student VALUES ('Pam', 85, 85)")
