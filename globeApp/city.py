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

# "INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark