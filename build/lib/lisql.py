import mysql.connector


def create_connection():
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


def create_remote_connection(host, user, password):
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

def create_database(mydb, name):
    cursor = mydb.cursor()
    create_db_query = f'CREATE DATABASE {name}'
    print(f'Executing command: {create_db_query}')
    try:
        cursor.execute(create_db_query)
        mydb.commit()
        print(f'Database {name} created successfully!')
    except mysql.connector.errors.DatabaseError:
        print('Database already exists')
    except Exception as e:
        print(f'Something else went wrong: {e}')
    return mydb

def connect_remote_database(host, username, password, database):
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        print(f"Connected to {host} successfully!")
        return mydb
    except Exception as e:
        print(f"Error connecting to {host}: {e}")

def drop_database(mydb, name):
    cursor = mydb.cursor()
    drop_db_query = f'DROP DATABASE IF EXISTS {name}'
    print(f'Executing command: {drop_db_query}')
    try:
        cursor.execute(drop_db_query)
        print(f'Database {name} dropped successfully!')
    except mysql.connector.errors.DatabaseError:
        print(f'Database {name} does not exist')
    except Exception as e:
        print(f'Something else went wrong: {e}')

def connect_database(mydb, name):
    try:
        mydb.database = name
        print('Connection established')
        return mydb
    except mysql.connector.errors.DatabaseError:
        print('Database does not exist')
    except (mysql.connector.errors.InterfaceError, mysql.connector.errors.ProgrammingError) as e:
        print(f'Connection error: {e}')
    except Exception as e:
        print(f'Something else went wrong: {e}')
    return None

def show_tables(mydb):
    cursor = mydb.cursor()
    cursor.execute("SHOW TABLES")
    tables = [table[0] for table in cursor]
    print(tables)
    return tables

def show_databases(mydb):
    cursor = mydb.cursor()
    cursor.execute("SHOW DATABASES")
    databases = [database[0] for database in cursor]
    print(databases)
    return databases



def select_data(mydb, table_name, columns):
    cursor = mydb.cursor()
    column_list = ", ".join(columns)
    select_query = f"SELECT {column_list} FROM {table_name}"
    cursor.execute(select_query)
    row = cursor.fetchone()
    while row is not None:
        yield row
        row = cursor.fetchone()

def insert_data(mydb, table_name, values):
    cursor = mydb.cursor()
    value_list = ", ".join(["%s"] * len(values))
    insert_query = f"INSERT INTO {table_name} VALUES ({value_list})"
    try:
        cursor.execute(insert_query, values)
        mydb.commit()
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error inserting data: {e}")

def drop_table(mydb, table_name):
    cursor = mydb.cursor()
    drop_query = f"DROP TABLE IF EXISTS {table_name}"
    try:
        cursor.execute(drop_query)
        mydb.commit()
        print(f"Table {table_name} dropped successfully!")
    except mysql.connector.errors.ProgrammingError:
        print(f"Table {table_name} does not exist")
    except Exception as e:
        print(f"Something else went wrong: {e}")

def delete_data(mydb, table_name, condition):
    cursor = mydb.cursor()
    delete_query = f"DELETE FROM {table_name} WHERE {condition}"
    try:
        cursor.execute(delete_query)
        mydb.commit()
        print(f"{cursor.rowcount} row(s) deleted successfully!")
    except Exception as e:
        print(f"Error deleting data: {e}")

def update_data(mydb, table_name, column_values, condition):
    cursor = mydb.cursor()
    column_value_pairs = [f"{col} = %s" for col in column_values.keys()]
    set_clause = ", ".join(column_value_pairs)
    update_query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
    try:
        cursor.execute(update_query, tuple(column_values.values()))
        mydb.commit()
        print(f"{cursor.rowcount} row(s) updated successfully!")
    except Exception as e:
        print(f"Error updating data: {e}")

def execute_query(mydb, query, fetch=False):
    cursor = mydb.cursor()
    try:
        cursor.execute(query)
        mydb.commit()
        if fetch:
            results = cursor.fetchall()
            return results
        else:
            print(f"{cursor.rowcount} row(s) affected!")
    except Exception as e:
        print(f"Error executing query: {e}")

def describe_table(mydb, table_name):
    cursor = mydb.cursor()
    describe_query = f"DESCRIBE {table_name}"
    cursor.execute(describe_query)
    table_info = cursor.fetchall()
    for info in table_info:
        print(info)
    return table_info

def describe_database(mydb):
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


def help(func=None):
    if func is None:
        print("Available functions:")
        print("- create_connection(): Creates a local connection to a SQLite database.")
        print("- create_remote_connection(host, user, password): Creates a remote connection to a SQLite database on a specified host.")
        print("- create_database(mydb, name): Creates a new database with the specified name in the local or remote connection.")
        print("- connect_remote_database(host, username, password, database): Connects to a remote database on a specified host.")
        print("- drop_database(mydb, name): Deletes the database with the specified name from the local or remote connection.")
        print("- connect_database(mydb, name): Connects to an existing database with the specified name in the local or remote connection.")
        print("- show_tables(mydb): Displays a list of tables in the connected database.")
        print("- show_databases(mydb): Displays a list of all databases in the connected server.")
        print("- select_data(mydb, table_name, columns): Retrieves data from the specified columns in the specified table.")
        print("- insert_data(mydb, table_name, values): Inserts data into the specified table.")
        print("- drop_table(mydb, table_name): Deletes the specified table from the connected database.")
        print("- delete_data(mydb, table_name, condition): Deletes data from the specified table that meets the specified condition.")
        print("- update_data(mydb, table_name, column_values, condition): Updates data in the specified table that meets the specified condition.")
        print("- execute_query(mydb, query, fetch=False): Executes the specified SQL query.")
        print("- describe_database(mydb): Displays information about the connected database.")
        print("- describe_table(mydb, table_name): Displays information about the specified table in the connected database.")
    elif func == create_connection:
        print("create_connection():\n")
        print("Creates a local connection to a SQLite database.")
        print("\nUsage:")
        print("  conn = create_connection()")
        print("\nReturns:")
        print("  A connection object that can be used to interact with the database.")
    elif func == create_remote_connection:
        print("create_remote_connection(host, user, password):\n")
        print("Creates a remote connection to a SQLite database on a specified host.")
        print("\nArgs:")
        print("  host (str): The host name or IP address of the server running the SQLite database.")
        print("  user (str): The username to use when connecting to the remote database.")
        print("  password (str): The password to use when connecting to the remote database.")
        print("\nUsage:")
        print("  conn = create_remote_connection('example.com', 'myuser', 'mypassword')")
        print("\nReturns:")
        print("  A connection object that can be used to interact with the database.")
    elif func == create_database:
        print("create_database(mydb, name):\n")
        print("Creates a new database with the specified name in the local or remote connection.")
        print("\nArgs:")
        print("  mydb (connection object): The connection object to the database.")
        print("  name (str): The name to use for the new database.")
        print("\nUsage:")
        print("  create_database(conn, 'my_new_db')")
        print("\nReturns:")
        print("  None")
    elif func == connect_remote_database:
        print("connect_remote_database(host, username, password, database):\n")
        print("Connects to a remote database on a specified host.")
        print("\nArgs:")
        print("- host: The host name or IP address of the remote server.")
        print("- username: The username used to authenticate with the remote server.")
        print("- password: The password used to authenticate with the remote server.")
        print("- database: The name of the remote database to connect to.")
    elif func == drop_database:
        print("drop_database(mydb, name):\n")
        print("Deletes the database with the specified name from the local or remote connection.")
        print("\nArgs:")
        print("- mydb: The connection object created by create_connection(), create_remote_connection(), or connect_remote_database().")
        print("- name: The name of the database to delete.")
    elif func == connect_database:
        print("connect_database(mydb, name):\n")
        print("Connects to an existing database with the specified name in the local or remote connection.")
        print("\nArgs:")
        print("- mydb: The connection object created by create_connection(), create_remote_connection(), or connect_remote_database().")
        print("- name: The name of the database to connect to.")
    elif func == show_tables:
        print("show_tables(mydb):\n")
        print("Displays a list of tables in the connected database.")
        print("\nArgs:")
        print("- mydb: The connection object created by create_connection(), create_remote_connection(), or connect_remote_database().")
    elif func == show_databases:
        print("show_databases(mydb):\n")
        print("Displays a list of all databases in the connected server.")
        print("\nArgs:")
        print("- mydb: The connection object created by create_connection(), create_remote_connection(), or connect_remote_database().")
    elif func == select_data:
        print("select_data(mydb, table_name, columns):\n")
        print("Retrieves data from the specified columns in the specified table.")
        print("\nArgs:")
        print("- mydb: The connection object created by create_connection(), create_remote_connection(), or connect_remote_database().")
        print("- table_name: The name of the table to retrieve data from.")
        print("- columns: A list of column names to retrieve data from. If not specified, all columns will be returned.")
    elif func == insert_data:
        print("insert_data(mydb, table_name, values):\n")
        print("Inserts data into the specified table.")
        print("\nArgs:")
        print("- mydb: The connection object created by create_connection(), create_remote_connection(), or connect_remote_database().")
        print("- table_name: The name of the table to insert data into.")
        print("- values: A list of tuples, where each tuple represents a row of data to be inserted.")
    elif func == drop_table:
        print("drop_table(mydb, table_name):\n")
        print("Deletes the specified table from the connected database.")
        print("\nArgs:")
        print("- mydb: The connection object created by create_connection(), create_remote_connection(), or connect_remote_database().")
        print("- table_name: The name of the table to delete.")
    elif func == delete_data:
        print("delete_data(mydb, table_name, condition):\n")
        print("Deletes data from the specified table that meets the specified condition.")
        print("\nArgs:")
        print("- mydb: the database connection object.")
        print("- table_name: the name of the table to delete data from.")
        print("- condition: the condition that data must meet in order to be deleted.")

    elif func == update_data:
        print("update_data(mydb, table_name, column_values, condition):\n")
        print("Updates data in the specified table that meets the specified condition.")
        print("\nArgs:")
        print("- mydb: the database connection object.")
        print("- table_name: the name of the table to update data in.")
        print("- column_values: a dictionary containing the column names and values to update.")
        print("- condition: the condition that data must meet in order to be updated.")

    elif func == execute_query:
        print("execute_query(mydb, query, fetch=False):\n")
        print("Executes the specified SQL query.")
        print("\nArgs:")
        print("- mydb: the database connection object.")
        print("- query: the SQL query to execute.")
        print("- fetch: a boolean indicating whether or not to fetch the results of the query.")

    elif func == describe_database:
        print("describe_database(mydb):\n")
        print("Displays information about the connected database.")
        print("\nArgs:")
        print("- mydb: the database connection object.")

    elif func == describe_table:
        print("describe_table(mydb, table_name):\n")
        print("Displays information about the specified table in the connected database.")
        print("\nArgs:")
        print("- mydb: the database connection object.")
        print("- table_name: the name of the table to describe.")

