#  App starting point - Main
#  pip install Flask

from flask import Flask, request, jsonify 
import country
# Using flask frame work
app = Flask(__name__)


# Read API
@app.route('/countries')
def getCountries():
    return country.getCountries()

# Execute on the terminal
if __name__ =='__main__':
    app.run()