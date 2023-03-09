#  Define all functions related to country API

from flask import Flask, request, jsonify
import services


def getcities():
    data = []
    for row in services.getcities():
        data.append({
            "CityId": row[0],
            "Name": row[1],
            "CountryId": row[2],
            "Capital": row[3],
            "FirstLandmark": row[4],
            "SecondLandmark": row[5],
            "ThirdLandmark": row[6]
        })
    return jsonify(data)


def createcity(data):
    services.createcity(data)
    return jsonify({'Message': "City created"})



def deletecity(cityid):
    services.deletecity(cityid)
    return jsonify({'Message': "City deleted"})


def updatecity(data):
    services.updatecity(data)
    return jsonify({'Message': "City updated"})