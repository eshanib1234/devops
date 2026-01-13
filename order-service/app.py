from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Order Service is running"

@app.route("/order")
def order():
    return jsonify({"service": "Order"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
