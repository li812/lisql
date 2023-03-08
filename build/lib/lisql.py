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
    cursor.execute("SHOW DATABASES")
    databases = [database[0] for database in cursor]
    for database in databases:
        print(f"Tables in database {database}:")
        cursor.execute(f"USE {database}")
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor]
        for table in tables:
            print(f"- {table}")
        print()


def help():
    print("Available functions:")
    print("- create_connection()")
    print("- create_remote_connection(host, user, password)")
    print("- create_database(mydb, name)")
    print("- connect_remote_database(host, username, password, database)")
    print("- drop_database(mydb, name)")
    print("- connect_database(mydb, name)")
    print("- show_tables(mydb)")
    print("- show_databases(mydb)")
    print("- select_data(mydb, table_name, columns)")
    print("- insert_data(mydb, table_name, values)")
    print("- drop_table(mydb, table_name)")
    print("- delete_data(mydb, table_name, condition)")
    print("- update_data(mydb, table_name, column_values, condition)")
    print("- execute_query(mydb, query, fetch=False)")
    print("- describe_database(mydb)")
    print("- describe_table(mydb, table_name)")

