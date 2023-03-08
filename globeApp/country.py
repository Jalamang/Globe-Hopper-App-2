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



def createcountry(data):
    services.createcountry(data)
    return jsonify({'Message': "Country created"})


def deletecountry(countryId):
    services.deletecountry(countryId)
    return jsonify({'Message': "Country deleted"})