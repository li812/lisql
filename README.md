lisql is a Python package that provides a simple interface to connect, create, drop, and manipulate data in a MySQL database. This package is developed with MySQL Connector/Python and provides easy-to-use functions to establish connections, create databases, tables, and insert, update and select data from a MySQL database.

Installation

To install lisql, you can use pip. Open your terminal or command prompt and enter the following command:

sh
Copy code
pip install lisql
Usage

To use lisql, you can import the package in your Python code and call the functions according to your requirements. The following functions are available in lisql:

Create Connection
creacon() - Establishes a connection to the MySQL server with default configuration.
creacuscon(host, username, password) - Establishes a custom connection to the MySQL server by providing the host, username, and password.
Create Database
creadb(name) - Creates a new database with the given name.
Drop Database
dropdb(name) - Drops the database with the given name.
Connect to Database
condb(name) - Connects to the database with the given name.
cuscondb(host, username, password, dbname) - Connects to a custom database by providing the host, username, password, and dbname.
Create Table
create_table(table_name, columns) - Creates a new table with the given table_name and columns.
Drop Table
drop_table(table_name) - Drops the table with the given table_name.
Insert Data
insert_data(table_name, values) - Inserts new data into the table with the given table_name.
Select Data
select_data(table_name, columns) - Selects data from the table with the given table_name and columns.
Update Data
update_data(table_name, column_values, condition) - Updates data in the table with the given table_name, column_values, and condition.
Example

Here's an example that demonstrates the usage of lisql:

python
Copy code
import lisql

# Establish a connection
lisql.creacon()

# Create a database
lisql.creadb('mydatabase')

# Connect to the database
lisql.condb('mydatabase')

# Create a table
lisql.create_table('mytable', 'id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT')

# Insert data into the table
lisql.insert_data('mytable', ('John', 30))
lisql.insert_data('mytable', ('Jane', 25))
lisql.insert_data('mytable', ('Bob', 40))

# Select data from the table
lisql.select_data('mytable', ['name', 'age'])

# Update data in the table
lisql.update_data('mytable', {'age': 31}, 'name = "John"')

# Drop the table
lisql.drop_table('mytable')

# Drop the database
lisql.dropdb('mydatabase')
License

This project is licensed under the MIT License - see the LICENSE file for details.