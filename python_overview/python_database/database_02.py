import sqlite3

def tables_in_sqlite_db(conn):
    # auxiliaty function to list the table names accoriding to the DB connection provided
    cursor_in = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [
        v[0] for v in cursor_in.fetchall()
        if v[0] != "sqlite_sequence"
    ]
    cursor_in.close()
    return tables


connection = sqlite3.connect("survey.db")  # Use the SQLite Browser to navigate through 'survey.db'
cursor = connection.cursor()

# tables available in our database
tables_db = tables_in_sqlite_db(connection)  # print(tables_in_sqlite_db(connection))
print('Available Tables: ', tables_db)

# from Site print the values for .lat and .long
# get the data
cursor.execute("SELECT Site.lat, Site.long FROM Site;")  # in execute we put the actual SQL command we want - remember this is a string so no variable names here
results = cursor.fetchall()
col_names = [name[0] for name in cursor.description]  # see the output for cursor.description

print('Table: {0}\nAttributes: {1}'.format("Site", col_names))
print('Values:')
for r in results:
    print(r)



cursor.close()
connection.close()