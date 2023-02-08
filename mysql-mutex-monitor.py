import mysql.connector
import time

# Connect to the MySQL database
cnx = mysql.connector.connect(user='username', password='password',
                              host='hostname', database='performance_schema')
cursor = cnx.cursor()

while True:
    # Query the performance_schema.events_waits_current table to get the mutex contention information
    query = "SELECT object_type, object_name, count_star FROM performance_schema.events_waits_current WHERE object_type = 'MUTEX'"
    cursor.execute(query)

    # Print the results
    for (object_type, object_name, count_star) in cursor:
        print("Object Type: {}\tObject Name: {}\tContention Count: {}".format(object_type, object_name, count_star))

    # Wait for 10 seconds before running the query again
    time.sleep(10)

# Close the cursor and connection
cursor.close()
cnx.close()
