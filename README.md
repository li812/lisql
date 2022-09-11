# lisql
 
## INSTALATION
Run the following to install

'''python
pip install lisql
'''

##Usage
'''python
import lisql

#To create default connection
    lisql.creacon()

#To create custom connection
    lisql.creacuscon(host, username, password)

#To create a database
    lisql.creadb(databasename)

#To drop a database
    lisql.dropdb(databasename)

#To connect a database in default connection
    lisql.condb(database_name)

#To connect a database in custom connection
    lisql.cuscondb(host, username, password, name)


