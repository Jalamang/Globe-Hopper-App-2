#  App starting point - Main
#  pip install Flask

from flask import Flask, request, jsonify 
import country, city
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
@app.route('/countries/<int:countryid>', methods=['DELETE'])
def deletecountry(countryid):
    return country.deletecountry(countryid)


# # # Read API
@app.route('/countries', methods=['PUT'])
def updatecountry():
    data = request.json
    return country.updatecountry(data)




# Cities Details

# Read API
@app.route('/cities')
def getcities():
    return city.getcities()


# # Read API
@app.route('/cities', methods=['POST'])
def createcity():
    data = request.json
    return city.createcity(data)


# # # Read API
@app.route('/cities/<int:cityid>', methods=['DELETE'])
def deletecity(cityid):
    return city.deletecity(cityid)


# Execute on the terminal
if __name__ =='__main__':
    app.run(debug=True)