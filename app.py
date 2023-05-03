from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Chat con mi Agente de Google Colab"

@app.route("/message", methods=["POST"])
def message():
    message = request.json["message"]
    response = requests.post("http://localhost:8080/respond", json={"message": message}).json()
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
