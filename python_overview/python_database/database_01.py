import sqlite3 as lite
import sys
'''
Make sure ot install sqlite3 so you can import it
SQLite can be also downloaded here: https://www.sqlite.org/download.html
There is a user friendly interface for SQLite (SQLite Browser): https://sqlitebrowser.org/dl/
    We can use SQLiteBrowser to navigate through our database as well
'''
con = None

try:
    con = lite.connect('test.db')  # let us connect to a test.db
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')  # and execute a select in its version
    data = cur.fetchone()
    print("SQLite version: %s" % data)
except:
    print("Error %s:" % sys.exc_info()[0])
    sys.exit(1)
finally:
    if con:
        con.close()  # after we are done, we should close the connection with the database, always.
