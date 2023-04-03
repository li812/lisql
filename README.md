# `lisql`

![logo](https://user-images.githubusercontent.com/68907011/229516295-04088400-302d-4849-bc48-9fd327800566.png)

`lisql` is a Python package that provides a simple and intuitive interface to work with MySQL databases. It can be used to perform various operations such as creating and dropping databases and tables, inserting and selecting data, and executing SQL queries. `lisql` can also be used in various fields where data is stored in MySQL databases, such as web development, data analytics, business intelligence, and more. With its easy-to-use functions for connecting to, querying, and modifying databases, `lisql` can help developers and analysts efficiently work with MySQL databases in their projects. Additionally, `lisql` can be integrated with other Python libraries and tools, such as Pandas and Scikit-learn, to provide more advanced data manipulation and analysis capabilities.

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
## Examples
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
This program connects to a local and remote MySQL server, connects to databases on each server, performs various database operations, and retrieves information about tables and databases.

### Here's an example program that demonstrates how to use lisql with pandas and numpy on two servers:
```
import lisql
import pandas as pd
import numpy as np

# create connections to two MySQL servers
conn1 = lisql.create_remote_connection('server1.example.com', 'user1', 'password1')
conn2 = lisql.create_remote_connection('server2.example.com', 'user2', 'password2')

# create databases on each server
lisql.create_database(conn1, 'mydb1')
lisql.create_database(conn2, 'mydb2')

# connect to databases on each server
db1 = lisql.connect_database(conn1, 'mydb1')
db2 = lisql.connect_database(conn2, 'mydb2')

# create tables on each database
lisql.execute_query(db1, 'CREATE TABLE mytable1 (id INT, value FLOAT)')
lisql.execute_query(db2, 'CREATE TABLE mytable2 (id INT, value FLOAT)')

# insert data into each table
data1 = np.random.rand(100, 2)
data2 = np.random.rand(100, 2)
df1 = pd.DataFrame(data1, columns=['id', 'value'])
df2 = pd.DataFrame(data2, columns=['id', 'value'])
lisql.insert_data(db1, 'mytable1', df1)
lisql.insert_data(db2, 'mytable2', df2)

# select data from each table and combine with pandas
query1 = 'SELECT * FROM mytable1'
query2 = 'SELECT * FROM mytable2'
result1 = lisql.select_data(db1, query1)
result2 = lisql.select_data(db2, query2)
df3 = pd.concat([pd.DataFrame(result1), pd.DataFrame(result2)], axis=1)

# print results
print(df3.head())

```
### Here's an example of using lisql to train a machine learning model using scikit-learn on more than two servers:
```
import lisql
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Create connections to multiple MySQL servers
server1 = lisql.create_remote_connection('server1.com', 'user1', 'pass1')
server2 = lisql.create_remote_connection('server2.com', 'user2', 'pass2')
server3 = lisql.create_remote_connection('server3.com', 'user3', 'pass3')

# Connect to multiple databases on different servers
db1 = lisql.connect_remote_database(server1, 'database1')
db2 = lisql.connect_remote_database(server2, 'database2')
db3 = lisql.connect_remote_database(server3, 'database3')

# Query data from multiple tables on different databases and servers
data1 = lisql.select_data(db1, 'table1', ['col1', 'col2', 'col3'])
data2 = lisql.select_data(db2, 'table2', ['col4', 'col5', 'col6'])
data3 = lisql.select_data(db3, 'table3', ['col7', 'col8', 'col9'])

# Merge the data into a single DataFrame using pandas and numpy
df1 = pd.DataFrame(list(data1), columns=['col1', 'col2', 'col3'])
df2 = pd.DataFrame(list(data2), columns=['col4', 'col5', 'col6'])
df3 = pd.DataFrame(list(data3), columns=['col7', 'col8', 'col9'])
df = pd.concat([df1, df2, df3], axis=1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, :-1], df.iloc[:, -1], test_size=0.2, random_state=42)

# Train a machine learning model using scikit-learn on the combined data
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model performance on the test set
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('Mean squared error:', mse)

```
In this example, we create connections to three different MySQL servers and connect to three different databases on these servers. We then query data from three different tables on these databases and merge the data into a single DataFrame using pandas and numpy. We split the data into training and testing sets and train a machine learning model using scikit-learn on the combined data. Finally, we evaluate the model performance on the test set.

### Here's a sample code snippet that demonstrates how you can use lisql with TensorFlow to train a machine learning model on data stored in multiple databases and servers:
```
import lisql
import tensorflow as tf
import pandas as pd

# Create connections to databases and servers
conn1 = lisql.create_remote_connection('host1', 'user1', 'password1')
conn2 = lisql.create_remote_connection('host2', 'user2', 'password2')

# Extract data from databases and servers
data1 = pd.read_sql_query("SELECT * FROM table1", conn1)
data2 = pd.read_sql_query("SELECT * FROM table2", conn2)

# Preprocess data
# ...

# Train machine learning model using TensorFlow
model = tf.keras.Sequential([...])
model.compile(...)
model.fit(data, labels, epochs=10, validation_data=(val_data, val_labels))

# Evaluate model on test data
test_data = pd.read_sql_query("SELECT * FROM test_table", conn1)
test_labels = pd.read_sql_query("SELECT label FROM test_table", conn2)
test_loss, test_acc = model.evaluate(test_data, test_labels, verbose=2)
print('Test accuracy:', test_acc)

```
In this example, we first create connections to two remote MySQL servers using create_remote_connection(). We then use Pandas and SQL queries to extract data from the servers and preprocess the data. We then train a machine learning model using TensorFlow and evaluate the model on test data extracted from one of the servers.

Note that this is just an example, and you can use other data science technologies such as Apache Spark or PyTorch with lisql in a similar way.

## For any questions, bug reports, or feedback, please feel free to contact the developers via:
### Email: aliahammad0812@outlook.com 

### Instagram: https://www.instagram.com/the_raptor_rider_/ 

