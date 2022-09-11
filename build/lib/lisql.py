from contextlib import nullcontext
import mysql.connector
import contextlib

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
