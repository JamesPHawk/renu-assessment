from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/renu-fibonacci": {"origins": "http://localhost:4173"}})

@app.route("/renu-fibonacci", methods=["POST"])
def calc_fibonacci():
    data = request.get_json()

    if not data or "value" not in data:
        return jsonify({"error": "Missing 'value' field"}), 400

    try:
        value = int(data["value"])
    except ValueError:
        return jsonify({"error": "Value must be an integer"}), 400

    # Stubbed logic (replace with real processing)
    result = {
        "index": value,
        "value": value * 2  # example "computation"
    }

    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)