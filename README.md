# `lisql`

The `lisql` package is a Python library that provides a simple interface for interacting with MySQL databases using the mysql-connector-python library. It allows users to perform various operations on MySQL databases such as creating and connecting to databases, creating tables, inserting and retrieving data, updating and deleting data, and executing custom SQL queries.

Using `lisql` provides benefits over other similar packages as it provides an easy-to-use and streamlined interface for performing common operations on MySQL databases. The package is also lightweight, making it ideal for small to medium-sized projects that require working with MySQL databases.

## Requirements:
Python 3.6 or higher
mysql-connector-python library (version 8.0 or higher)

You can install the mysql-connector-python library using pip:
```commandline
pip install mysql-connector-python

```
## Installation:

To install the `lisql` package, you can follow the steps below:

1: Open a terminal or command prompt on your machine.
```commandline
python --version

```
2: Make sure you have  `Python 3.6` or higher installed on your machine. You can check your Python version by running the above command.


3: Install the `lisql` package using pip:
```commandline
pip install lisql
```

This will automatically install the required `mysql-connector-python` library as a dependency.

4: You can now start using the `lisql` package in your Python scripts by importing it:
```commandline
import lisql

```

5: If you want to use a remote MySQL server, make sure you have the necessary credentials (host, username, and password) to connect to the server.

6: To connect to a remote MySQL server, you can use the `create_remote_connection()` function, passing in the host, username, and password as arguments:
```
mydb = lisql.create_remote_connection(host, username, password)
```

7: Once you have a database connection, you can use the `connect_database()` function to connect to a specific database:
```commandline
mydb = lisql.connect_database(mydb, 'mydatabase')

```
8: You can now start executing SQL queries using the `lisql` package.
Note: If you encounter any errors during installation, make sure you have the necessary permissions to install Python packages on your machine. You can also try running the installation command with administrative privileges (e.g., using sudo on Linux or macOS).

## Usage:

### 1: Creating a Connection
To create a connection to a MySQL server, you can use the create_connection() function:
```
import lisql

mydb = lisql.create_connection()
```
You can also create a connection to a remote server by passing in the host, username, and password:
```
mydb = lisql.create_remote_connection(host, username, password)

```
### 2: Connecting to a Database
To connect to a database, you can use the connect_database() function:

```commandline
mydb = lisql.connect_database(mydb, 'mydatabase')

```
### 3: Connecting to a remote Database
To creates a connection to a remote MySQL database using the specified host, user, and password.
```commandline
mydb = lisql.connect_remote_database(mydb, 'mydatabase')
```
### 4: Creating a Database
To create a new database, you can use the create_database() function:
```commandline
mydb = lisql.create_database(mydb, 'mydatabase')
```
### 5: Showing Tables and Databases
To show the tables in the current database, you can use the show_tables() function:
```commandline
tables = lisql.show_tables(mydb)

```
To show the databases on the MySQL server, you can use the show_databases() function:
```commandline
databases = lisql.show_databases(mydb)

```
### 6: Selecting Data
To select data from a table, you can use the select_data() function:
```commandline
data = lisql.select_data(mydb, 'mytable', ['column1', 'column2'])
for row in data:
    print(row)

```
### 7: Inserting Data
To insert data into a table, you can use the insert_data() function:

```commandline
lisql.insert_data(mydb, 'mytable', ['value1', 'value2'])

```

### 8: Updating Data
To update data in a table, you can use the update_data() function:
```commandline
lisql.update_data(mydb, 'mytable', {'column1': 'value1'}, 'column2 = "value2"')

```

### 9: Deleting Data
To delete data from a table, you can use the delete_data() function:

```
lisql.delete_data(mydb, 'mytable', 'column1 = "value1"')

```

### 10: Dropping a Table or Database
To drop a table, you can use the drop_table() function:

```commandline
lisql.drop_table(mydb, 'mytable')

```
To drop a database, you can use the drop_database() function:

```
lisql.drop_database(mydb, 'mydatabase')
```
### 11: Executing a Query
To execute a custom SQL query, you can use the execute_query() function:

```commandline
lisql.execute_query(mydb, 'SELECT * FROM mytable', fetch=True)

```

### 12: Describing a Table
To describe the structure of a table, you can use the describe_table() function:
```commandline
lisql.describe_table(mydb, 'mytable')
```

### 12: Describing a Database
To describe the structure of a database, you can use the describe_database() function:
```commandline
lisql.describe_database(mydb)
```

## Here are some usage examples:

### 1: Creating a connection to a local MySQL server:
```
import lisql

# Create a connection
mydb = lisql.create_connection()

# Connect to a database
mydb = lisql.connect_database(mydb, 'mydatabase')

# Select data from a table
data = lisql.select_data(mydb, 'mytable', ['column1', 'column2'])
for row in data:
    print(row)
```
### 2: Creating a connection to a remote MySQL server:
```commandline
import lisql

# Create a connection to a remote server
mydb = lisql.create_remote_connection('remote_host', 'remote_user', 'remote_password')

# Connect to a database
mydb = lisql.connect_remote_database(mydb, 'mydatabase')

# Select data from a table
data = lisql.select_data(mydb, 'mytable', ['column1', 'column2'])
for row in data:
    print(row)

```
### 3: Inserting data into a table:
```commandline
import lisql

# Create a connection
mydb = lisql.create_connection()

# Connect to a database
mydb = lisql.connect_database(mydb, 'mydatabase')

# Insert data into a table
lisql.insert_data(mydb, 'mytable', ['value1', 'value2'])

```

### 4: Updating data in a table:
```commandline
import lisql

# Create a connection
mydb = lisql.create_connection()

# Connect to a database
mydb = lisql.connect_database(mydb, 'mydatabase')

# Update data in a table
lisql.update_data(mydb, 'mytable', {'column1': 'new_value'}, 'column2 = "value2"')

```

### 5: Deleting data from a table:
```commandline
import lisql

# Create a connection
mydb = lisql.create_connection()

# Connect to a database
mydb = lisql.connect_database(mydb, 'mydatabase')

# Delete data from a table
lisql.delete_data(mydb, 'mytable', 'column1 = "value1"')

```


### 6: Creating a new database:
```commandline
import lisql

# Create a connection
mydb = lisql.create_connection()

# Create a new database
mydb = lisql.create_database(mydb, 'mydatabase')

```
### 7: Creating a new table:
```commandline
import lisql

# Create a connection
mydb = lisql.create_connection()

# Connect to a database
mydb = lisql.connect_database(mydb, 'mydatabase')

# Create a new table
lisql.create_table(mydb, 'mytable', {'column1': 'VARCHAR(255)', 'column2': 'INT'})

```
### 8: Dropping a table:
```commandline
import lisql

# Create a connection
mydb = lisql.create_connection()

# Connect to a database
mydb = lisql.connect_database(mydb, 'mydatabase')

# Drop a table
lisql.drop_table(mydb, 'mytable')

```

### 9: Dropping a database:
```commandline
import lisql

# Create a connection
mydb = lisql.create_connection()

# Drop a database
lisql.drop_database(mydb, 'mydatabase')

```

### Here's an example program that demonstrates connecting to multiple servers and databases:
```
import lisql

# Create a connection to a local MySQL server with default user and password values
local_db = lisql.create_connection()

# Create a connection to a remote MySQL server with specified host, user, and password values
remote_db = lisql.create_remote_connection(host="example.com", user="myusername", password="mypassword")

# Connect to a database on the local server
lisql.connect_database(local_db, "my_local_database")

# Connect to a database on the remote server
lisql.connect_remote_database(remote_db, host="example.com", username="myusername", password="mypassword", database="my_remote_database")

# List all tables in the current database on the local server
local_tables = lisql.show_tables(local_db)
print("Tables in local database:")
for table in local_tables:
    print(table)

# List all tables in the current database on the remote server
remote_tables = lisql.show_tables(remote_db)
print("Tables in remote database:")
for table in remote_tables:
    print(table)

# Select data from a table in the local database
local_data = lisql.select_data(local_db, "my_table", ["column1", "column2"])
for row in local_data:
    print(row)

# Insert data into a table in the remote database
remote_data = [("value1", "value2"), ("value3", "value4")]
lisql.insert_data(remote_db, "my_table", remote_data)

# Delete data from a table in the remote database where a condition is true
lisql.delete_data(remote_db, "my_table", "column1 = 'value1'")

# Update data in a table in the local database where a condition is true
lisql.update_data(local_db, "my_table", {"column2": "new_value"}, "column1 = 'value1'")

# Execute a SQL query on the remote database and fetch all rows
remote_query = "SELECT * FROM my_table"
remote_result = lisql.execute_query(remote_db, remote_query, fetch=True)
for row in remote_result:
    print(row)

# Describe a table in the local database
local_description = lisql.describe_table(local_db, "my_table")
print("Columns in local table:")
for column in local_description:
    print(column)

# Describe the remote database
remote_description = lisql.describe_database(remote_db)
print("Tables in remote database:")
for table in remote_description:
    print(table)

```


## For any questions, bug reports, or feedback, please feel free to contact the developers via the GitHub repository:

### https://github.com/li812/lisql

or by email at aliahammad0812@outlook.com .
