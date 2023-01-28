from flask import Flask, abort

app = Flask(__name__)


@app.before_request
def service_not_available():
    abort(503)
