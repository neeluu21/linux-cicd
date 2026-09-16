from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Backend is working successfully"


@app.route("/api/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Backend is running"
    })


@app.route("/api/users")
def users():
    return jsonify({
        "users": [
            {
                "id": 1,
                "name": "Neel"
            },
            {
                "id": 2,
                "name": "DevOps User"
            }
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
