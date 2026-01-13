from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Product Service is running"

@app.route("/product")
def product():
    return jsonify({"service": "Product"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
