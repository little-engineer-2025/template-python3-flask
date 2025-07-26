#!/usr/bin/env python3

import threading
import time
from flask import request
import pytest
import requests

import my_service.service as service

from requests.exceptions import ConnectionError

def create_app():
    return service.app

def stop_app():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@pytest.fixture()
def app():
    _app = create_app()
    _app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield _app

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
