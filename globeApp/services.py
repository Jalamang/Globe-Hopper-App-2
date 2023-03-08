# Define all services for city and country

from flask import Flask, request, jsonify
import dbconn





#  Gets all records from the country entity using sequel
def getcountries():
    #Open connection
    dbconn.con._open_connection()
    myCursor = dbconn.con.cursor()
    
    myCursor.execute("SELECT * FROM Country")
    result = myCursor.fetchall()
    
    #Close connection
    myCursor.close()
    dbconn.con.close()
    
    return result
    
# Add a country 
def createcountry(data):
    #Open connection
    dbconn.con._open_connection()
    myCursor = dbconn.con.cursor()
    
    countryid = data['CountryId']
    name = data['Name']
    population = data['Population']
    continent = data['Continent']
    
    
    sql = "INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s, %s, %s, %s)"
    val = (countryid, name, population, continent)
    myCursor.execute(sql, val)
    
    #Close connection
    myCursor.close()
    dbconn.con.close()
    
    
# Add a country 
def deletecountry(countryId):
     #Open connection
    dbconn.con._open_connection()
    myCursor = dbconn.con.cursor()
    
    sql = "DELETE FROM Country WHERE CountryId = %s"
    id = countryId
    myCursor.execute(sql, (id,))
    
    dbconn.con.commit()

    #Close connection
    myCursor.close()
    dbconn.con.close()
    
