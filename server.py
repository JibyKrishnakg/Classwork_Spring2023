from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def server_status():
    return "Server on"

@app.route("/info", methods = ["GET"])
def info_route():
    return "This server was written for BME 547"

if __name__ == '__main__':
    app.run()