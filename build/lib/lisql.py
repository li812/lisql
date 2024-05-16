print("""
                                                                                                   
888      d8b  .d8888b.   .d88888b.  888           
888      Y8P d88P  Y88b d88P" "Y88b 888           
888          Y88b.      888     888 888           
888      888  "Y888b.   888     888 888           
888      888     "Y88b. 888     888 888           
888      888       "888 888 Y8b 888 888           
888      888 Y88b  d88P Y88b.Y8b88P 888           
88888888 888  "Y8888P"   "Y888888"  88888888     2.2
                               Y8b                
                                                                                                                                                                                                 
""")

import importlib

def check_and_install_mysql_connector():
    try:
        importlib.import_module('mysql.connector')
    except ImportError:
        print("mysql-connector-python is not installed. Installing it now...")
        try:
            import pip
            pip.main(['install', 'mysql-connector-python'])

        except Exception as e:
            print("Error installing mysql-connector-python:", str(e))

check_and_install_mysql_connector()

import mysql.connector

def create_connection():
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        if mydb.is_connected():
            print('MySQL connected')
        else:
            print('MySQL not connected')
        return mydb
    except mysql.connector.Error as e:
        print(f"Error creating local connection: {e}")
        return None

def create_remote_connection(host, user, password):
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        if mydb.is_connected():
            print('MySQL connected')
        else:
            print('MySQL not connected')
        return mydb
    except mysql.connector.Error as e:
        print(f"Error creating remote connection: {e}")
        return None

def create_database(mydb, name, transaction=True):
    cursor = mydb.cursor()
    create_db_query = f'CREATE DATABASE {name}'
    print(f'Executing command: {create_db_query}')
    try:
        if transaction:
            mydb.start_transaction()  # Start the transaction explicitly
            
        cursor.execute(create_db_query)
        
        if transaction:
            mydb.commit()  # Commit the transaction if transaction=True
            
        print(f'Database {name} created successfully!')
    except mysql.connector.Error as e:
        if transaction:
            mydb.rollback()  # Roll back the transaction if an error occurs
        if e.errno == mysql.connector.errorcode.ER_DB_CREATE_EXISTS:
            print(f'Database {name} already exists')
        else:
            print(f'Something else went wrong: {e}')
    except Exception as e:
        print(f'Something else went wrong: {e}')
    return mydb


def connect_remote_database(host, username, password, database, transaction=True):
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        print(f"Connected to {host} successfully!")
        if transaction:
            mydb.autocommit = False  # Disable autocommit to enable transactions
        return mydb
    except mysql.connector.Error as e:
        print(f"Error connecting to {host}: {e}")
        return None


def drop_database(mydb, name, transaction=True):
    cursor = mydb.cursor()
    drop_db_query = f'DROP DATABASE IF EXISTS {name}'
    print(f'Executing command: {drop_db_query}')
    try:
        if transaction:
            mydb.start_transaction()  # Start the transaction explicitly
            
        cursor.execute(drop_db_query)
        
        if transaction:
            mydb.commit()  # Commit the transaction if transaction=True
            
        print(f'Database {name} dropped successfully!')
    except mysql.connector.Error as e:
        if transaction:
            mydb.rollback()  # Roll back the transaction if an error occurs
        if e.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print(f'Database {name} does not exist')
        else:
            print(f'Something else went wrong: {e}')


def connect_database(mydb, name, transaction=True):
    try:
        mydb.database = name
        print('Connection established')

        if transaction:
            mydb.autocommit = False  # Disable autocommit to enable transactions
        
        return mydb
    except mysql.connector.Error as e:
        print(f"Error connecting to {name}: {e}")
    except (mysql.connector.InterfaceError, mysql.connector.ProgrammingError) as e:
        print(f'Connection error: {e}')
    except Exception as e:
        print(f'Something else went wrong: {e}')
    return None


def show_tables(mydb):
    try:
        cursor = mydb.cursor()
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor]
        print(tables)
        return tables
    except mysql.connector.Error as e:
        print(f"Error while showing tables: {e}")
        return []
    
    
def create_table(mydb, table_name, columns, transaction=True):
    cursor = mydb.cursor()
    column_definitions = ", ".join(columns)
    create_table_query = f"CREATE TABLE {table_name} ({column_definitions})"
    print(f'Executing command: {create_table_query}')
    try:
        if transaction:
            mydb.start_transaction()  # Start the transaction explicitly
            
        cursor.execute(create_table_query)
        
        if transaction:
            mydb.commit()  # Commit the transaction if transaction=True
            
        print(f'Table {table_name} created successfully!')
    except mysql.connector.Error as e:
        if transaction:
            mydb.rollback()  # Roll back the transaction if an error occurs
        print(f"Error creating table: {e}")


def drop_table(mydb, table_name, transaction=True):
    cursor = mydb.cursor()
    drop_table_query = f'DROP TABLE IF EXISTS {table_name}'
    print(f'Executing command: {drop_table_query}')
    try:
        if transaction:
            mydb.start_transaction()  # Start the transaction explicitly
            
        cursor.execute(drop_table_query)
        
        if transaction:
            mydb.commit()  # Commit the transaction if transaction=True
            
        print(f'Table {table_name} dropped successfully!')
    except mysql.connector.Error as e:
        if transaction:
            mydb.rollback()  # Roll back the transaction if an error occurs
        print(f"Error dropping table: {e}")


def show_databases(mydb):
    try:
        cursor = mydb.cursor()
        cursor.execute("SHOW DATABASES")
        databases = [database[0] for database in cursor]
        print(databases)
        return databases
    except mysql.connector.Error as e:
        print(f"Error while showing databases: {e}")
        return []

def show_table(db, table_name):
    try:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        if len(rows) == 0:
            print(f"No data found in table '{table_name}'")
        else:
            print(f"Contents of table '{table_name}':")
            for row in rows:
                print(row)
    except mysql.connector.Error as e:
        print(f"Error displaying table '{table_name}': {e}")


def select_data(mydb, table_name, columns):
    try:
        cursor = mydb.cursor()
        column_list = ", ".join(columns)
        select_query = f"SELECT {column_list} FROM {table_name}"
        cursor.execute(select_query)
        row = cursor.fetchone()
        while row is not None:
            yield row
            row = cursor.fetchone()
    except mysql.connector.Error as e:
        print(f"Error while selecting data: {e}")
        return

def insert_data(mydb, table_name, values, transaction=True):
    try:
        cursor = mydb.cursor()
        value_list = ", ".join(["%s"] * len(values))
        insert_query = f"INSERT INTO {table_name} VALUES ({value_list})"
        
        if transaction:
            mydb.start_transaction()  # Start the transaction explicitly
            
        cursor.execute(insert_query, values)
        
        if transaction:
            mydb.commit()  # Commit the transaction if transaction=True
            
        print("Data inserted successfully!")
        
    except mysql.connector.Error as e:
        if transaction:
            mydb.rollback()  # Roll back the transaction if an error occurs
        print(f"Error inserting data: {e}")




def delete_data(mydb, table_name, condition, transaction=True):
    try:
        cursor = mydb.cursor()
        delete_query = f"DELETE FROM {table_name} WHERE {condition}"
        
        if transaction:
            mydb.start_transaction()  # Start the transaction explicitly
            
        cursor.execute(delete_query)
        
        if transaction:
            mydb.commit()  # Commit the transaction if transaction=True
            
        print(f"{cursor.rowcount} row(s) deleted successfully!")
        
    except mysql.connector.Error as e:
        if transaction:
            mydb.rollback()  # Roll back the transaction if an error occurs
        print(f"Error deleting data: {e}")


def update_data(mydb, table_name, column_values, condition, transaction=True):
    try:
        cursor = mydb.cursor()
        column_value_pairs = [f"{col} = %s" for col in column_values.keys()]
        set_clause = ", ".join(column_value_pairs)
        update_query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        
        if transaction:
            mydb.start_transaction()  # Start the transaction explicitly
            
        cursor.execute(update_query, tuple(column_values.values()))
        
        if transaction:
            mydb.commit()  # Commit the transaction if transaction=True
            
        print(f"{cursor.rowcount} row(s) updated successfully!")
        
    except mysql.connector.Error as e:
        if transaction:
            mydb.rollback()  # Roll back the transaction if an error occurs
        print(f"Error updating data: {e}")


def execute_query(mydb, query, fetch=False, transaction=True):
    try:
        cursor = mydb.cursor()
        
        if transaction:
            mydb.start_transaction()  # Start the transaction explicitly
            
        cursor.execute(query)
        
        if transaction:
            mydb.commit()  # Commit the transaction if transaction=True
            
        if fetch:
            results = cursor.fetchall()
            return results
        else:
            print(f"{cursor.rowcount} row(s) affected!")
            
    except mysql.connector.Error as e:
        if transaction:
            mydb.rollback()  # Roll back the transaction if an error occurs
        print(f"Error executing query: {e}")
        return []


def describe_table(mydb, table_name):
    try:
        cursor = mydb.cursor()
        describe_query = f"DESCRIBE {table_name}"
        cursor.execute(describe_query)
        table_info = cursor.fetchall()
        for info in table_info:
            print(info)
        return table_info
    except mysql.connector.Error as e:
        print(f"Error describing table: {e}")
        return []

def describe_database(mydb):
    try:
        cursor = mydb.cursor()
        cursor.execute("SELECT DATABASE()")
        database_name = cursor.fetchone()[0]
        print(f"Database: {database_name}")
        print("Tables:")
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor]
        for table in tables:
            describe_query = f"DESCRIBE {table}"
            cursor.execute(describe_query)
            table_info = cursor.fetchall()
            print(f"{table}:")
            for info in table_info:
                print(info)
    except mysql.connector.Error as e:
        print(f"Error describing database: {e}")


########################   Start of Aggregate functions     #######################

def select_count(mydb, table, column):
    cursor = mydb.cursor()
    query = f"SELECT COUNT({column}) FROM {table}"
    try:
        cursor.execute(query)
        result = cursor.fetchone()[0]
        return result
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")
        return None


def select_sum(mydb, table, column):
    cursor = mydb.cursor()
    query = f"SELECT SUM({column}) FROM {table}"
    try:
        cursor.execute(query)
        result = cursor.fetchone()[0]
        return result
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")
        return None


def select_avg(mydb, table, column):
    cursor = mydb.cursor()
    query = f"SELECT AVG({column}) FROM {table}"
    try:
        cursor.execute(query)
        result = cursor.fetchone()[0]
        return result
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")
        return None


def select_min(mydb, table, column):
    cursor = mydb.cursor()
    query = f"SELECT MIN({column}) FROM {table}"
    try:
        cursor.execute(query)
        result = cursor.fetchone()[0]
        return result
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")
        return None


def select_max(mydb, table, column):
    cursor = mydb.cursor()
    query = f"SELECT MAX({column}) FROM {table}"
    try:
        cursor.execute(query)
        result = cursor.fetchone()[0]
        return result
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")
        return None


########################   End of Aggregate functions     #######################



########################   Start of help    #######################
def help(func=None):
    if func is None:
        print("LiSQL Package - Python Package for Interacting with MySQL Databases")
        print("Version: 2.2")
        print("Description: LiSQL is a Python package that simplifies working with MySQL databases by providing various functions for connection management, database operations, table operations, and data manipulation.")
        print("\nAvailable functions:")
        # Group 1: Connection Management
        print("\nConnection Management:")
        print("- create_connection(): Creates a local connection to a MySQL database.")
        print("  Example: create_connection()")
        print("  This function establishes a connection to a local MySQL database and returns the connection object.")
        print("- create_remote_connection(host, user, password): Creates a remote connection to a MySQL database on a specified host.")
        print("  Example: create_remote_connection('remote_host', 'remote_user', 'remote_password')")
        print("  This function establishes a remote connection to a MySQL database on the specified host and returns the connection object.")        
        print("- connect_remote_database(host, username, password, database): Connects to a remote MySQL database on a specified host.")
        print("  Example: connect_remote_database('remote_host', 'remote_user', 'remote_password', 'remote_db')")
        print("  This function connects to a remote MySQL database on the specified host with the specified username, password, and database name, and returns the connection object.")       
        # Group 2: Database Operations
        print("\nDatabase Operations:")
        print("- create_database(mydb, name): Creates a new database with the specified name in the local or remote connection.")
        print("  Example: create_database(mydb, 'new_database')")
        print("  This function creates a new database with the specified name in the connected local or remote MySQL connection.")        
        print("- drop_database(mydb, name): Deletes the database with the specified name from the local or remote connection.")
        print("  Example: drop_database(mydb, 'existing_database')")
        print("  This function drops the database with the specified name from the connected local or remote MySQL connection.")
        
        print("- connect_database(mydb, name): Connects to an existing database with the specified name in the local or remote connection.")
        print("  Example: connect_database(mydb, 'existing_database')")
        print("  This function connects to an existing database with the specified name in the connected local or remote MySQL connection.")
        
        print("- show_databases(mydb): Displays a list of all databases in the connected server.")
        print("  Example: show_databases(mydb)")
        print("  This function shows a list of all databases in the connected local or remote MySQL server.")
        # Group 3: Table Operations
        print("\nTable Operations:")
        print("- show_tables(mydb): Displays a list of tables in the connected database.")
        print("  Example: show_tables(mydb)")
        print("  This function shows a list of tables in the connected local or remote MySQL database.")
        print("- create_table(mydb, table_name, columns, transaction=True): Creates a table with the specified columns.")
        print("  Example: columns = ['id INT PRIMARY KEY', 'name VARCHAR(255)', 'age INT']")
        print("           create_table(mydb, 'students', columns, transaction=True)")
        print("  This function creates a new table with the specified name and columns in the connected local or remote MySQL database.")        
        print("- drop_table(mydb, table_name, transaction=True): Deletes the specified table from the connected database.")
        print("  Example: drop_table(mydb, 'students', transaction=True)")
        print("  This function drops the specified table from the connected local or remote MySQL database.")
        print("- describe_table(mydb, table_name): Displays information about the specified table in the connected database.")
        print("  Example: describe_table(mydb, 'students')")
        print("  This function describes the specified table in the connected local or remote MySQL database.")

        # Group 4: Data Manipulation
        print("\nData Manipulation:")
        print("- select_data(mydb, table_name, columns): Retrieves data from the specified columns in the specified table.")
        print("  Example: columns = ['name', 'age']")
        print("           for data in select_data(mydb, 'students', columns):")
        print("               print(data)")
        print("  This function retrieves data from the specified columns in the specified table in the connected local or remote MySQL database.")
        
        print("- insert_data(mydb, table_name, values, transaction=True): Inserts data into the specified table.")
        print("  Example: values = (1, 'John Doe', 25)")
        print("           insert_data(mydb, 'students', values, transaction=True)")
        print("  This function inserts data into the specified table in the connected local or remote MySQL database.")
        
        print("- delete_data(mydb, table_name, condition, transaction=True): Deletes data from the specified table that meets the specified condition.")
        print("  Example: condition = 'age > 30'")
        print("           delete_data(mydb, 'students', condition, transaction=True)")
        print("  This function deletes data from the specified table that meets the specified condition in the connected local or remote MySQL database.")
        
        print("- update_data(mydb, table_name, column_values, condition, transaction=True): Updates data in the specified table that meets the specified condition.")
        print("  Example: column_values = {'name': 'John Smith', 'age': 32}")
        print("           condition = 'id = 1'")
        print("           update_data(mydb, 'students', column_values, condition, transaction=True)")
        print("  This function updates data in the specified table that meets the specified condition in the connected local or remote MySQL database.")
        
        print("- execute_query(mydb, query, fetch=False, transaction=True): Executes the specified SQL query.")
        print("  Example: query = 'SELECT * FROM students WHERE age > 30'")
        print("           result = execute_query(mydb, query, fetch=True, transaction=True)")
        print("  This function executes the specified SQL query in the connected local or remote MySQL database.")
        
        print("- describe_database(mydb): Displays information about the connected database, including all tables and their structures.")
        print("  Example: describe_database(mydb)")
        print("  This function describes the connected database, including all tables and their structures in the connected local or remote MySQL database.")
        
        # Group 5: Aggregate Functions
        print("\nAggregate Functions:")
        print("- select_count(mydb, table, column): Returns the count of non-null values in the specified column of the specified table.")
        print("  Example: count = select_count(mydb, 'students', 'age')")
        print("  This function returns the count of non-null values in the specified column of the specified table in the connected local or remote MySQL database.")
        
        print("- select_sum(mydb, table, column): Returns the sum of values in the specified column of the specified table.")
        print("  Example: total_age = select_sum(mydb, 'students', 'age')")
        print("  This function returns the sum of values in the specified column of the specified table in the connected local or remote MySQL database.")
        
        print("- select_avg(mydb, table, column): Returns the average of values in the specified column of the specified table.")
        print("  Example: avg_age = select_avg(mydb, 'students', 'age')")
        print("  This function returns the average of values in the specified column of the specified table in the connected local or remote MySQL database.")
        
        print("- select_min(mydb, table, column): Returns the minimum value in the specified column of the specified table.")
        print("  Example: min_age = select_min(mydb, 'students', 'age')")
        print("  This function returns the minimum value in the specified column of the specified table in the connected local or remote MySQL database.")
        
        print("- select_max(mydb, table, column): Returns the maximum value in the specified column of the specified table.")
        print("  Example: max_age = select_max(mydb, 'students', 'age')")
        print("  This function returns the maximum value in the specified column of the specified table in the connected local or remote MySQL database.")
        
        print("\nFor more details about each function, you can use the 'help' function followed by the function name.")
        print("Example: help(create_table)")
        print("This will display detailed information about the 'create_table' function.")
        print("\nNote: For remote database connections, make sure the necessary MySQL privileges are granted to the specified user and that the MySQL server allows remote connections.")
    else:
        if func.__doc__:
            print(func.__doc__)
        else:
            print("No documentation available for this function.")

########################   End of help    #######################


def __version__():
    return 2.2
