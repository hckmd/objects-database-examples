# Runs a SELECT query to retrieve rows from fruit table
cursor.execute('SELECT * FROM fruit')
rows = cursor.fetchall()

for row in rows:
    print(row)