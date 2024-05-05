import wikipedia
from flask import Flask, request, make_response
import json

app = Flask(__name__)


@app.route('/CelebrityName', methods=['GET'])
def getCelebrityInfo(request):
    celebrity_name = request.args.get('celebrityName')
    if not celebrity_name:
        return make_response(json.dumps({"error": "Celebrity Name is missing"}), 400)

    result = wikipedia.summary(celebrity_name, sentences=2)
    response = {
        "celebrityName": celebrity_name,
        "content": result
    }

    return make_response(json.dumps(response), 200, {'Content-Type': 'application/json'})