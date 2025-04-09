from flask import Flask, jsonify, request
from math_logic import sum, multiply, divide, find_max, find_min

app = Flask(__name__)

@app.route("/compute", methods=["GET"])
def compute():
    ans1 = multiply(1, 2)
    ans2 = divide(4, ans1)
    ans3 = find_max(ans2, ans1)
    ans4 = find_min(4, 5)

    return jsonify({
        "multiply(1,2)": ans1,
        "divide(4, multiply)": ans2,
        "max(divide, multiply)": ans3,
        "min(4,5)": ans4,
        "message": "Calculations complete"
    })

@app.route("/")
def index():
    return "Welcome to the Flask Math API!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
