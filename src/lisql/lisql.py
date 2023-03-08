#Start of lisql package source code
from contextlib import nullcontext
import mysql.connector
import contextlib
import tkinter as tk
import webbrowser
from PIL import Image, ImageTk, ImageDraw

#Start of create connection
def creacon():
  global mydb
  mydb = mysql.connector.connect(
      host = 'localhost',
      user = "root",
      password = ""
      )
  if mydb!=nullcontext:
    print("MySQL Connected")
  else:
    print("MySQL Not Connected")
#End of create connection

#Start of create custom connection
def creacuscon(host, username, password):
  global mydb
  mydb = mysql.connector.connect(
      host = host,
      user = username,
      password = password
      )
  if mydb!=nullcontext:
    print("MySQL Connected")
  else:
    print("MySQL Not Connected")
#End of create custom connection

#Start of create database
def creadb(name):
    exe = mydb.cursor()
    cdb ="CREATE DATABASE "
    sql = cdb+name
    print ("Executing command : ",sql)
    try:
        exe.execute(sql)
        mydb.commit()
        print("DATABASE ",name," has successfully been created !")
    except mysql.connector.errors.DatabaseError:
      print("Database already exists")
    except:
      print("Something else went wrong, check your server configuration")
#Start of create database

#Start of drop database
def dropdb(name):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    )
    exe = mydb.cursor()
    cdb ="DROP DATABASE "
    sql = cdb+name
    print ("Executing command : ",sql)
    try:
        exe.execute(sql)
        mydb.commit()
        print("DATABASE ",name," has successfully been dropped !")
    except mysql.connector.errors.DatabaseError:
      print("Database doesn't exists")
    except:
      print("Something else went wrong, check your server configuration")
#End of drop database


#Start of connect database
def condb(name):
  try: 
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = name
    )
    print("Connection established")
  except mysql.connector.errors.DatabaseError:
      print("Database doesn't exists")
  except:
      print("Something else went wrong, check your server configuration")

#end of connect database

#Start of connect database in custom connection
def cuscondb(host, username, password,dbname):
  try: 
    global mydb
    mydb = mysql.connector.connect(
    host=host,
    user=username,
    password=password,
    database = dbname
    )
    print("Connection established")
  except mysql.connector.errors.DatabaseError:
      print("Database doesn't exists")
  except:
      print("Something else went wrong, check your server configuration")

#end of connect database in custom connection

#Start of create table
def create_table(table_name, columns):
    exe = mydb.cursor()
    sql = "CREATE TABLE {} ({})".format(table_name, columns)
    print("Executing command: ", sql)
    try:
        exe.execute(sql)
        mydb.commit()
        print("Table {} created successfully!".format(table_name))
    except mysql.connector.errors.DatabaseError as error:
        print("Failed to create table {}: {}".format(table_name, error))

#End of create table

#Start of drop table
def drop_table(table_name):
    exe = mydb.cursor()
    sql = "DROP TABLE {}".format(table_name)
    print("Executing command: ", sql)
    try:
        exe.execute(sql)
        mydb.commit()
        print("Table {} dropped successfully!".format(table_name))
    except mysql.connector.errors.DatabaseError as error:
        print("Failed to drop table {}: {}".format(table_name, error))
#End of drop table

#start of insert data
def insert_data(table_name, values):
    exe = mydb.cursor()
    placeholders = ', '.join(['%s'] * len(values))
    sql = "INSERT INTO {} VALUES ({})".format(table_name, placeholders)
    print("Executing command: ", sql)
    try:
        exe.execute(sql, values)
        mydb.commit()
        print("Data inserted successfully!")
    except mysql.connector.errors.DatabaseError as error:
        print("Failed to insert data: {}".format(error))
#end of insert data

#start of select data
def select_data(table_name, columns):
    exe = mydb.cursor()
    if columns == "*":
        sql = "SELECT * FROM {}".format(table_name)
    else:
        columns_str = ",".join(columns)
        sql = "SELECT {} FROM {}".format(columns_str, table_name)
    print("Executing command: ", sql)
    try:
        exe.execute(sql)
        result = exe.fetchall()
        for row in result:
            print(row)
    except mysql.connector.errors.DatabaseError as error:
        print("Failed to fetch data from {}: {}".format(table_name, error))
#End of select data

# Start of update data
def update_data(table_name, column_values, condition):
    exe = mydb.cursor()
    set_values = ', '.join([f'{col} = {val}' for col, val in column_values.items()])
    sql = f"UPDATE {table_name} SET {set_values} WHERE {condition}"
    print("Executing command: ", sql)
    try:
        exe.execute(sql)
        mydb.commit()
        print(f"{exe.rowcount} row(s) updated in table {table_name}")
    except mysql.connector.errors.DatabaseError as error:
        print("Failed to update data in table {}: {}".format(table_name, error))

# End of update data

#start of delete data
def delete_data(table_name, condition):
    exe = mydb.cursor()
    sql = "DELETE FROM {} WHERE {}".format(table_name, condition)
    print("Executing command: ", sql)
    try:
        exe.execute(sql)
        mydb.commit()
        print(f"{exe.rowcount} row(s) deleted from table {table_name}")
    except mysql.connector.errors.DatabaseError as error:
        print("Failed to delete data from table {}: {}".format(table_name, error))
#end of delete data


#start of close connection
def close_con():
    global mydb
    if mydb is not None:
        mydb.close()
        print("Connection closed successfully!")
    else:
        print("No connection found to close.")
#end of close connection

#start of show_databases
def show_databases():
    exe = mydb.cursor()
    sql = "SHOW DATABASES"
    print("Executing command: ", sql)
    try:
        exe.execute(sql)
        result = exe.fetchall()
        print("Databases:")
        for db in result:
            print(db[0])
    except mysql.connector.errors.DatabaseError as error:
        print("Failed to show databases: {}".format(error))
#end of show_databases

#Start of show tables
def show_tables():
    exe = mydb.cursor()
    sql = "SHOW TABLES"
    exe.execute(sql)
    tables = exe.fetchall()
    if len(tables) > 0:
        print("Tables in the current database:")
        for table in tables:
            print(table[0])
    else:
        print("No tables found in the current database")
#end of show tables

#Start of execute_query
def execute_query(query, fetch=False):
    cursor = mydb.cursor()
    try:
        cursor.execute(query)
        mydb.commit()
        print("Query executed successfully!")
        if fetch:
            result = cursor.fetchall()
            for row in result:
                print(row)
    except mysql.connector.errors.DatabaseError as error:
        print("Failed to execute query: {}".format(error))
#End of execute_query

#Start of Describe Table
def describe_table(table_name):
    exe = mydb.cursor()
    sql = "DESCRIBE {}".format(table_name)
    print("Executing command: ", sql)
    try:
        exe.execute(sql)
        result = exe.fetchall()
        for row in result:
            print(row)
    except mysql.connector.errors.ProgrammingError as error:
        print("Failed to describe table {}: {}".format(table_name, error))
#end of Describe Table



#Start of about
def about():
  class AboutMeWindow(tk.Tk):
      def __init__(self, photo_path, name, email):
          super().__init__()
          self.title("About Me")
          self.geometry("400x480")

          # Open image and create circle mask
          image = Image.open(photo_path)
          image = image.resize((200, 200))  # Resize image to fit window
          mask = Image.new("L", (200, 200), 0)
          draw = ImageDraw.Draw(mask)
          draw.ellipse((0, 0, 200, 200), fill=255)

          # Apply mask to image
          image.putalpha(mask)
          photo = ImageTk.PhotoImage(image)

          # Create label for photo
          photo_label = tk.Label(self, image=photo)
          photo_label.image = photo
          photo_label.pack(pady=10)

          # Create label for name
          name_label = tk.Label(self, text=name, font=("Arial", 16))
          name_label.pack(pady=5)

          # Create label for email
          email_label = tk.Label(self, text=email, font=("Arial", 12))
          email_label.pack(pady=5)

          # Create button to send email
          def send_email():
              webbrowser.open(f"mailto:{email}")
          email_button = tk.Button(self, text="Send Email", command=send_email)
          email_button.pack(pady=5)

          # Create button to open LinkedIn profile
          def open_linkedin():
              webbrowser.open(f"https://www.linkedin.com/in/ali-ahammad-li0812/")
          linkedin_button = tk.Button(self, text="View LinkedIn Profile", command=open_linkedin)
          linkedin_button.pack(pady=5)

          # Create button to open GitHub profile
          def open_github():
              webbrowser.open(f"https://github.com/li812")
          github_button = tk.Button(self, text="View GitHub Profile", command=open_github)
          github_button.pack(pady=5)

          # Create button to open Instagram profile
          def open_instagram():
              webbrowser.open(f"https://www.instagram.com/the_raptor_rider_/")
          instagram_button = tk.Button(self, text="View Instagram Profile", command=open_instagram)
          instagram_button.pack(pady=5)



  if __name__ == '__main__':
      window = AboutMeWindow("src/pic.png", "Ali Ahammad", "aliahammad0812@outlook.com")
      close_button = tk.Button(window, text="Close", command=window.destroy)
      close_button.pack(pady=5)
      window.mainloop()
#End of about 
#End of lisql package source code

