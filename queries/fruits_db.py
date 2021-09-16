import sqlite3 
# Connects to store.db database, creating it if it doesn't exist
connection = sqlite3.connect('store.db') 
cursor = connection.cursor()

# Creates a table called fruit
cursor.execute('CREATE TABLE fruit (id INT PRIMARY KEY, name TEXT, price_cents INT)')

# Inserts two rows into the fruit table: one for apple and one for pear
cursor.execute("INSERT INTO fruit VALUES (1,'apple', 100)")
cursor.execute("INSERT INTO fruit VALUES (2, 'pear', 90)")

# Commit the changes and close the connection with the database file
connection.commit()
connection.close()