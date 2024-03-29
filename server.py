from flask import Flask, request, json

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def server_status():
    return "Server on"

@app.route("/info", methods = ["GET"])
def info_route():
    return "This server was written for BME 547"

@app.route("/info", methods = ["POST"])
def HDL_route_handler():
    """
    in_data = {"name":<patient_name>, 
                "HDL_value":<HDL_result>}
    """
    from bloodcal import HDL_analysis
    in_data = request.get_json()
    diagnosis = HDL_analysis(in_data["HDL_value"])
    return diagnosis


@app.route("/add", methods = ["POST"])
def add_numbers():
    in_data = request.get_json()
    answer = in_data["a"] + in_data["b"]
    if answer < 0:
        return "The answer was less than zero.BAD", 400
    return jsonify(answer)


@app.route("/add_two/<a>/<b>", methods = ["GET"])
def add_two_handlere(a,b):
    answer = a + b
    return jsonify(answer)


if __name__ == '__main__':
    app.run()