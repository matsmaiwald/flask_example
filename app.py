from flask import Flask, request
import json

app = Flask(__name__)


def get_exponential(base, exponent):
    return base ** exponent


@app.route("/", methods=["GET"])
def instructions():
    response = """
    To use this app, send a post request with a json of the following format:
    {"base": "<number you want to use as base>",
     "exponent": "<number you want to use as exponent>"}
    and you will receive the result of raising the base to the power, as specified.
    Pretty cool, eh?!
    """
    return response


@app.route("/", methods=["POST"])
def post():
    record = json.loads(request.data)
    base, exponent = int(record["base"]), int(record["exponent"])
    exponential = get_exponential(base=base, exponent=exponent)

    return str(exponential)  # Flask does not like returning ints
