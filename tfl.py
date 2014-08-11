from flask import jsonify,render_template
import requests
import simplejson
import json

@app.route('/tfl')

@app.route('/post', methods = ['POST'])
def post():
    # Get the parsed contents of the form data
    json = request.json
    print(json)
    # Render template
    return jsonify(json)


# http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?Stopid=36012&ReturnList=Stoppointname,VehicleID,RegistrationNumber,LineName,DestinationName,EstimatedTime,ExpireTime
