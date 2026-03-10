
from flask import Flask, request, jsonify

app = Flask(__name__)

requests_db = []

@app.route("/")
def home():
    return {"message": "Juatz is live – Local Trust OS running."}

@app.route("/request", methods=["POST"])
def create_request():
    data = request.json
    requests_db.append(data)
    return {"status": "Request added", "data": data}

@app.route("/requests", methods=["GET"])
def list_requests():
    return jsonify(requests_db)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
