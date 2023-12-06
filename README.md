# WebsiteProject
Set up Database:  
Create Database:  
To create your database, in the MariaDB/mysql command line, do
```
source PATH_TO_FILE
```
where PATH_TO_FILE is the path to create_db.sql.  
Give Python Access to database:  
For your python to have permission to access your database, alter the credentials in db.py to reflect your MariaDB server credentials. For example:
```
user="root",
password="12345",
host="127.0.0.1",
port=3306,
database="City_Of_Williamston"
```
