from flask import Flask, request, jsonify
from flask_cors import CORS
from math import sqrt 

app = Flask(__name__)
CORS(app, resources={r"/renu-fibonacci": {"origins": "http://localhost:4173"}})

def big_fib(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]

def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    if(n == 0 or n == 1):
        return
    M = [[1, 1],
         [1, 0]]

    power(F, n // 2)
    multiply(F, F)

    if (n % 2 != 0):
        multiply(F, M)

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
    try:

        if value < -604 or value > 1476:
            return jsonify({"error": f"Input {value} exceeds maximum allowed Fibonacci input (1476)", "status": 500})
        elif value > 604:
            fib_value = big_fib(value)
        else:
            fib_value = fib(value)
        
        if value <= -50 or value >= 50:
            fib_value = f"{fib_value:.2e}"

        result = {
            "index": value,
            "value": fib_value
        }
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {e}", "status": 500})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)