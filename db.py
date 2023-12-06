#CMPE131_TeamStar
# Module Imports
import mariadb
import sys
import os

# Connect to MariaDB Platform
try:
    mydb = mariadb.connect(
        user="root",
        password="[YOUR MARIADB PASSWORD]",
        host="127.0.0.1",
        port=3306,
        database="City_Of_Williamston"
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

def get_db():
    return mydb;

