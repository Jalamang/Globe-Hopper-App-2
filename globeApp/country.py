#  Define all functions related to country API

from flask import Flask, request, jsonify
import services

def getcountries():
    data = []
    for row in services.getcountries():
        data.append({
            "countryId": row[0],
            "Name": row[1],
            "Population": row[2],
            "Continent": row[3]
        })
    return jsonify(data)


def getcountry(countryid):
    
    data = []
    for row in services.getcountry(countryid):
        data.append({
            "countryId": row[0],
            "Name": row[1],
            "Population": row[2],
            "Continent": row[3]
        })
    return  jsonify({'Message': "Country with ...is fetched"},{"Payload": data})


def getcountrybycontinent(continent_name):
    data = []
    for row in services.getcountrybycontinent(continent_name):
        data.append({
            "CountryId": row[0],
            "Name": row[1],
            "Population": row[2],
            "Continent": row[3]
        })
    return jsonify(data)

def createcountry(data):
    services.createcountry(data)
    return jsonify({'Message': "Country created"})


def deletecountry(countryid):
    services.deletecountry(countryid)
    return jsonify({'Message': "Country deleted"})


def updatecountry(data):
    services.updatecountry(data)
    return jsonify({'Message': "Country updated"})