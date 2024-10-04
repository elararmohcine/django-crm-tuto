import mysql.connector # type: ignore


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'mohcine',
    passwd = 'mohcine199917#'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a databse
cursorObject.execute("CREATE DATABASE crm")

print("All Done!")

