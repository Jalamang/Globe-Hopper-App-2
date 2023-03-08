# Define all services for city and country

from flask import Flask, request, jsonify
import dbconn





#  Gets all records from the country entity using sequel
def getcountries():
    #Open connection
    dbconn.con._open_connection()
    mycursor = dbconn.con.cursor()
    
    mycursor.execute("SELECT * FROM Country")
    result = myCursor.fetchall()
    
    #Close connection
    mycursor.close()
    dbconn.con.close()
    
    return result
    
# Add a country 
def createcountry(data):
    #Open connection
    dbconn.con._open_connection()
    mycursor = dbconn.con.cursor()
    
    countryid = data['CountryId']
    name = data['Name']
    population = data['Population']
    continent = data['Continent']
    
    
    sql = "INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s, %s, %s, %s)"
    val = (countryid, name, population, continent)
    mycursor.execute(sql, val)
    
    #Close connection
    myCursor.close()
    dbconn.con.close()
    
    
# Add a country 
def deletecountry(countryid):
     #Open connection
    dbconn.con._open_connection()
    mycursor = dbconn.con.cursor()
    
    sql = "DELETE FROM Country WHERE CountryId = %s"
    cid = countryid
    mycursor.execute(sql, (cid,))
    
    dbconn.con.commit()

    #Close connection
    mycursor.close()
    dbconn.con.close()
    
