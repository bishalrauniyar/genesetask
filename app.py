from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello Genese Solution! My CI/CD task is running!. Now I am updating the code to test the CI/CD pipeline. I am checking live 1"})

@app.route("/status")
def status():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)