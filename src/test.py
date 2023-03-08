import lisql
mydb = lisql.create_connection()
mydb = lisql.create_database(mydb, 'db2')
lisql.show_databases(mydb)
mydb = lisql.connect_database(mydb, 'db2')
lisql.describe_database(mydb)
lisql.help()
lisql.describe_table(mydb, 'user_details')