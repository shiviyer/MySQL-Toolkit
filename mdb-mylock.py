import mysql.connector
import time

# Connect to the MySQL database
cnx = mysql.connector.connect(user='<username>', password='<password>', host='<host>', database='<database>')
cursor = cnx.cursor()

# Define the query to fetch lock information from the performance schema
query = "SELECT THREAD_ID, SQL_TEXT, LOCK_TYPE, LOCK_MODE, LOCK_DURATION, SOURCE FROM performance_schema.data_locks WHERE LOCK_TYPE = 'Record'"

# Continuously run the query and fetch the lock information
while True:
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        thread_id = result[0]
        sql_text = result[1]
        lock_type = result[2]
        lock_mode = result[3]
        lock_duration = result[4]
        source = result[5]

        print("Thread ID: ", thread_id)
        print("SQL Query: ", sql_text)
        print("Lock Type: ", lock_type)
        print("Lock Mode: ", lock_mode)
        print("Lock Duration: ", lock_duration)
        print("Source: ", source)
        print("-----------------------------")

    # Sleep for 2 seconds before checking again
    time.sleep(2)

# Close the connection to the database
cursor.close()
cnx.close()
