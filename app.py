from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Nishant", "role": "Developer"},
    {"id": 2, "name": "Rahul", "role": "Tester"},
    {"id": 3, "name": "Amit", "role": "DevOps"}
]


@app.route("/")
def home():
    return "Backend is running!"


@app.route("/api/health")
def health():
    return jsonify({
        "status": "UP",
        "message": "Backend is healthy"
    })


@app.route("/api/users")
def get_users():
    return jsonify(users)


@app.route("/api/users/<int:user_id>")
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)

    return jsonify({
        "message": "User not found"
    }), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
