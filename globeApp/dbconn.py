# This file will connect to mysql DB

# python -m pip install mysql-connector-python

from mysql import connector
from decouple import config


con = connector.connect(
    host = config("host"),
    user = config("user"),
    password = config("password"),
    database = config("database")
)