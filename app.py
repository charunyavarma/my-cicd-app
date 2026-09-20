from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! CI/CD deployment successful!"

app.run(host="0.0.0.0", port=5000)
