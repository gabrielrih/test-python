'''
    SQLite test
    Reference: https://docs.python.org/3/library/sqlite3.html
'''
import sqlite3

# Starts a database in a file
#conn = sqlite3.connect('example.db')
# Starts database in memory
conn = sqlite3.connect(':memory:')

# Creates a cursor
cursor = conn.cursor()

# Creates a table
try:
    cursor.execute('CREATE TABLE Test (id int, value text)')
except:
    print("Table already exists!")

# Remove all rows from table 
cursor.execute("DELETE FROM Test")

# Insert rows of data
cursor.execute("INSERT INTO Test VALUES (1,'Value 1')")
cursor.execute("INSERT INTO Test VALUES (2,'Value 2')")
cursor.execute("INSERT INTO Test VALUES (3,'Value 3')")

# Save (commit) the changes
conn.commit()

# Get rows
for row in cursor.execute('SELECT * FROM Test ORDER BY id ASC'):
        print(row[0]) # first element
        print(row[1]) # second element

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()