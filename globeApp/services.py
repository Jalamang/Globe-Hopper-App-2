# Define all services for city and country

from flask import Flask, request, jsonify
import dbconn



#  Gets all records from the country entity using sequel
def getCountries():
    #Open connection
    dbconn.con._open_connection()
    myCursor = dbconn.con.cursor()
    
    myCursor.execute("SELECT * FROM Country")
    result = myCursor.fetchall()
    
    #Close connection
    myCursor.close()
    dbconn.con.close()
    
    return result
    
    

