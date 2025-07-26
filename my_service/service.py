#!/usr/bin/env python3
"""Hello world package"""
from flask import Flask
from .hellos import hellos_bp

VERSION = "v1"
SERVICE_NAME = "service"
PREFIX = "/api/" + SERVICE_NAME + "/" + VERSION

app = Flask(__name__)
app.register_blueprint(hellos_bp, url_prefix=PREFIX)

@app.errorhandler(404)
def not_found(error):
    """Default 404 error handler"""
    response = {
        "error": "Not Found",
        "status": 404,
        "message": error.description,
    }
    return response, 404

@app.route("/readyz", methods=["GET"])
def readyz():
    """Service readiness

    Return:
        200 if the service is ready to attend requests.
        500 if the service is is not ready to attend requests.
    """
    is_ready = True
    if is_ready:
        return "Ok", 200
    else:
        return "Not ready", 500

@app.route("/healthyz", methods=["GET"])
def healthz():
    """Service liveness

    Return:
        200 if the service is live.
        500 if the service is is not alive.
    """
    is_live = True
    if is_live:
        return "Ok", 200
    else:
        return "Not alive", 500
