#  App starting point - Main
#  pip install Flask

from flask import Flask, request, jsonify 
import country
# Using flask frame work
app = Flask(__name__)


# Read API
@app.route('/countries')
def getcountries():
    return country.getcountries()



# # Read API
@app.route('/countries', methods=['POST'])
def createcountry():
    data = request.json
    return country.createcountry(data)


# # # Read API
@app.route('/countries/<int:countryId>', methods=['DELETE'])
def deletecountry(countryId):
    return country.deletecountry(countryId)



# Execute on the terminal
if __name__ =='__main__':
    app.run(debug=True)