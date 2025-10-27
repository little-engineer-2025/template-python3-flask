#!/usr/bin/env python3
"""Hello world package"""
from flask import Flask
from .hellos import bp as hellos_bp

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

VERSION = "v1"
SERVICE_NAME = "service"
PREFIX = "/api/" + SERVICE_NAME + "/" + VERSION

app = Flask(__name__)

# https://prometheus.github.io/client_python/exporting/http/flask/
# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

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
    return "Not alive", 500
