import sqlite3


def make_connection(database_file, query):
    '''
    Common connection function that will fetch data with a given query in a specific DB
    The cursor will be closed at the end of it
    '''
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute(query)  # if id is available here we can also use    cursor.execute(query, [person_id])
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def add_name(database_file, new_person):
    '''
    The same way we select we can also modify our table with new records
    '''
    query = "INSERT INTO Person VALUES (?, ?, ?);"

    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute(query, list(new_person))
    cursor.close()
    connection.commit()
    connection.close()

def get_name(database_file, person_id):
    '''
    Here we get one specific record according to an ID
    Different from database_01 we are using variable names to compose our query,
        just make sure to compose one string at the end
    '''
    query = "SELECT personal || ' ' || family FROM Person WHERE id='" + person_id + "';"
    results = make_connection(database_file, query)
    return results[0][0]

# Insert a new name
add_name('survey.db', ('barrett', 'Mary', 'Barrett'))

# Check it exists
print("Full name for barrett:", get_name('survey.db', 'barrett'))

# Open SQLite Browser to see the new record there.