# Lisql Package

Lisql is a Python package that provides a simple interface for interacting with MySQL databases. It includes functions for creating connections, creating and dropping databases and tables, inserting and selecting data, updating and deleting rows, and more.

## Functions

- `creacon()`: creates a connection to a MySQL server on the localhost with default credentials.
- `creacuscon(host, username, password)`: creates a custom connection to a MySQL server with the provided host, username, and password.
- `creadb(name)`: creates a new MySQL database with the given name if it does not already exist.
- `dropdb(name)`: drops the MySQL database with the given name if it exists.
- `condb(name)`: connects to the MySQL database with the given name if it exists.
- `cuscondb(host, username, password, dbname)`: connects to the custom MySQL database with the provided host, username, password, and dbname.
- `create_table(table_name, columns)`: creates a new table in the currently connected MySQL database with the given table name and columns.
- `drop_table(table_name)`: drops the table with the given table name in the currently connected MySQL database.
- `insert_data(table_name, values)`: inserts a row of data into the table with the given table name and values.
- `select_data(table_name, columns)`: retrieves the data from the table with the given table name and columns.
- `update_data(table_name, column_values, condition)`: updates the rows in the table with the given table name that meet the given condition with the new column values.
- `delete_data(table_name, condition)`: deletes the rows in the table with the given table name that meet the given condition.
- `close_con()`: closes the connection to the MySQL database if it is open.
- `show_databases()`: retrieves a list of all databases on the MySQL server.
- `show_tables()`: retrieves a list of all tables in the currently selected database.
- `execute_query(query, fetch=False)`: executes a SQL query string using a cursor object.
- `describe_table(table_name)`: retrieves information about the columns of a table.
