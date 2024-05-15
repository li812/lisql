import sys
import mysql

def create_connection():
    try:
        # Try importing mysqlclient
        import MySQLdb as mysql_module
    except ImportError:
        try:
            # If mysqlclient is not available, try importing mysql.connector
            import mysql.connector as mysql_module
        except ImportError:
            # If neither mysqlclient nor mysql.connector is available, print an error message
            print("Neither 'mysqlclient' nor 'mysql.connector' is installed.")
            return None

    # MySQL connection parameters
    mysql_params = {
        'host': 'localhost',
        'user': 'root',
        'password': ''
    }

    try:
        mydb = mysql_module.connect(**mysql_params)
        if mydb.is_connected():
            print('MySQL connected')
        else:
            print('MySQL not connected')
        return mydb
    except mysql_module.Error as e:
        print(f"Error creating local connection: {e}")
        return None

# Test the function
create_connection()


