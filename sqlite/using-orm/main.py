'''
    SQLite test using ORM ()
    Reference: https://docs.python.org/3/library/sqlite3.html
'''
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# Create the database 
engine = create_engine('sqlite:///test.db', echo=True)

# Create users database
meta = MetaData()
users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('password',String)
)
meta.create_all(engine)

# Starts a connection
conn = engine.connect()

# Insert a row
insert = users.insert().values(name = 'Gabriel', password = 'thisIsThePass') # Generate query1
result = conn.execute(insert)

# Close the connection
conn.close()