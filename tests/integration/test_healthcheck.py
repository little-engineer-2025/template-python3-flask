#!/usr/bin/env python3

import requests

from .fixtures import app, client, runner


def test_readyz(client):
    """Test /readyz healthcheck"""
    response = client.get("http://127.0.0.1:5000/readyz")
    assert 200 == response.status_code
    assert "Ok" == response.text


def test_healthyz(client):
    """Test /healthyz healthcheck"""
    response = client.get("http://127.0.0.1:5000/healthyz")
    assert 200 == response.status_code
    assert "Ok" == response.text
