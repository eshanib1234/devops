from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/user")
def user():
    return jsonify({"service": "User"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
