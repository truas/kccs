import sqlite3

'''
The database returns the results of the query in response to the cursor.fetchall call
This result is a list with one entry for each record in the result set
'''


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


def get_name(database_file, person_id):
    '''
    Here we get one specific record according to an ID
    Different from database_01 we are using variable names to compose our query,
        just make sure to compose one string at the end
    '''
    query = "SELECT personal || ' ' || family FROM Person WHERE id='" + person_id + "';"
    results = make_connection(database_file, query)
    return results[0][0]

def get_allnames(database_file):
    '''
    Here we fetch all data in our table, regardless of id
    '''
    query = "SELECT personal || ' ' || family FROM Person;"
    results = make_connection(database_file, query)
    return results


print("Full name for dyer:", get_name('survey.db', 'dyer'))  # specific id

partial = get_allnames("survey.db")  # all results
for item in partial:
    print(item[0])