from flask import Flask, request, jsonify
from flask_cors import CORS
from math import sqrt 

app = Flask(__name__)
CORS(app, resources={r"/renu-fibonacci": {"origins": "http://localhost:4173"}})

def fib(n):
    res = (((1+sqrt(5))**abs(n))-((1-sqrt(5)))**abs(n))/(2**abs(n)*sqrt(5))
    if n < 0 and abs(n) % 2 == 0:
        res = res * -1
    return round(res)

@app.route("/renu-fibonacci", methods=["POST"])
def calc_fibonacci():
    data = request.get_json()

    if not data or "value" not in data:
        return jsonify({"error": "Missing 'value' field"}), 400

    try:
        value = int(data["value"])
    except ValueError:
        return jsonify({"error": "Value must be an integer"}), 400
    
    result = {
        "index": value,
        "value": fib(value)
    }

    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)