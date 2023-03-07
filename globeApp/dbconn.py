# This file will connect to mysql DB

# python -m pip install mysql-connector-python

# import mysql.connector
from mysql import connector

con = connector.connect(
    host = "localhost",
    user="ally",
    password="Ally@123",
    database="globehopperapp"
)