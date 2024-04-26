#!/usr/bin/python3
"""
Module: 0-select_states
Connects to a MySQL database and retrieves all states from the states table.
"""

import sys
import MySQLdb

def get_states(username, password, db_name):
    """Connects to MySQL database and retrieves all states."""
    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the SQL query to select all states
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)

    # Fetch all rows from the result
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1:]
    get_states(username, password, db_name)
