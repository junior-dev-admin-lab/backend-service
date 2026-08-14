from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/api/users")
def users():
    return jsonify([
        {"id": 1, "name": "Nishant"},
        {"id": 2, "name": "Rahul"}
    ])

@app.route("/api/health")
def health():
    return jsonify({
        "status": "UP",
        "message": "Backend is healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
