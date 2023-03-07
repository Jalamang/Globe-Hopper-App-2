#  Define all functions related to country API

from flask import Flask, request, jsonify
import services

def getCountries():
    result = services.getCountries()
    return jsonify(result)