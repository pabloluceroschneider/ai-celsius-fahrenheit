from flask import Flask, request, jsonify

from model import CelsiusFahrenheitModel

app = Flask(__name__)

cf_model = CelsiusFahrenheitModel()

@app.route("/")
def predict():
    q = request.args.get('q')
    
    y = cf_model.predict(q)
    
    return jsonify({ "celsius": q, "fahrenheit": y })
