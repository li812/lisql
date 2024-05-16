import lisql

db = lisql.create_connection()

db = lisql.connect_database(db, "university")

def insert_data(mydb, table_name, values):
    try:
        cursor = mydb.cursor()
        value_list = ", ".join(["%s"] * len(values))
        insert_query = f"INSERT INTO {table_name} VALUES ({value_list})"
        
            
        cursor.execute(insert_query, values)
        
        mydb.commit()  # Commit the transaction if transaction=True
            
        print("Data inserted successfully!")
        
    except mysql.connector.Error as e:
        mydb.rollback()  # Roll back the transaction if an error occurs
        print(f"Error inserting data: {e}")

def select_min(mydb, table, column, transaction=True):
    cursor = mydb.cursor()
    query = f"SELECT MIN({column}) FROM {table}"
    try:
        if transaction:
            mydb.start_transaction()  # Start the transaction explicitly
        
        cursor.execute(query)
        result = cursor.fetchone()[0]
        
        if transaction:
            mydb.commit()  # Commit the transaction if transaction=True
        
        return result
    except mysql.connector.Error as e:
        if transaction:
            mydb.rollback()  # Roll back the transaction if an error occurs
        print(f"Error executing query: {e}")
        return None

# #insert_data(db, "STUDENT", (1001, "Alice", "123 Main St", 1, 2))

# # Insert data into BRANCH table
# insert_data(db, "BRANCH", (1, "Computer Science", "Dr. Smith"))
# insert_data(db, "BRANCH", (2, "Electrical Engineering", "Dr. Johnson"))

# # Insert data into STUDENT table
# insert_data(db, "STUDENT", (1001, "Alice", "123 Main St", 1, 2))
# insert_data(db, "STUDENT", (1002, "Bob", "456 Elm St", 2, 1))
# insert_data(db, "STUDENT", (1003, "Charlie", "789 Oak St", 1, 2))
# insert_data(db, "STUDENT", (1004, "David", "101 Pine St", 2, 1))
# insert_data(db, "STUDENT", (1005, "Eva", "222 Maple St", 1, 2))
# insert_data(db, "STUDENT", (1006, "Frank", "333 Birch St", 2, 1))
# insert_data(db, "STUDENT", (1007, "Grace", "444 Cedar St", 1, 2))
# insert_data(db, "STUDENT", (1008, "Henry", "555 Walnut St", 2, 1))

# # Insert data into BOOK table
# insert_data(db, "BOOK", (1, "Python Programming", 1, "Tech Books", 1))
# insert_data(db, "BOOK", (2, "Network Security", 2, "Secure Press", 1))
# insert_data(db, "BOOK", (3, "Machine Learning Basics", 3, "AI Publications", 1))
# insert_data(db, "BOOK", (4, "Introduction to Robotics", 4, "Robo Books", 1))
# insert_data(db, "BOOK", (5, "Electrical Circuits", 5, "Circuit Co.", 2))
# insert_data(db, "BOOK", (6, "Database Management Systems", 6, "Data Books", 2))
# insert_data(db, "BOOK", (7, "Data Structures and Algorithms", 7, "Code Publishers", 1))
# insert_data(db, "BOOK", (8, "Artificial Intelligence", 8, "AI Publications", 1))

# # Insert data into AUTHOR table
# insert_data(db, "AUTHOR", (1, "John Smith", "USA", 40))
# insert_data(db, "AUTHOR", (2, "Jane Doe", "Canada", 35))
# insert_data(db, "AUTHOR", (3, "Alice Johnson", "UK", 45))
# insert_data(db, "AUTHOR", (4, "Bob Brown", "Australia", 50))

# # Insert data into BORROW table
# insert_data(db, "BORROW", (1001, 1, "2024-04-01"))
# insert_data(db, "BORROW", (1001, 7, "2024-03-15"))
# insert_data(db, "BORROW", (1003, 3, "2024-03-01"))
# insert_data(db, "BORROW", (1005, 4, "2024-02-05"))

# # Insert additional borrow records for testing other queries
# insert_data(db, "BORROW", (1002, 2, "2024-04-10"))
# insert_data(db, "BORROW", (1004, 5, "2024-04-15"))
# insert_data(db, "BORROW", (1006, 6, "2024-05-01"))
# insert_data(db, "BORROW", (1007, 8, "2024-04-05"))


#lisql.insert_data(db, "BORROW", (1007, 2, "2024-04-05"),transaction=True)
#lisql.insert_data(db, "BORROW", (1007, 3, "2024-04-05"),transaction=True)

#lisql.insert_data(db, "BORROW", (1007, 4, "2024-04-05"))

#lisql.show_table(db, "STUDENT")


#print(lisql.describe_database(db))

#print(lisql.select_max(db, "STUDENT", "USN"))

print(lisql.describe_table(db,"STUDENT"))