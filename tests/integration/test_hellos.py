#!/usr/bin/env python3

import os
import pytest
import werkzeug
import my_service.hellos as service
from .fixtures import app, client
from markupsafe import escape


class _:
    TEST_NAME = "john doe"
    BASE_URL = "http://localhost:5000/api/service/v1/hellos"


def test_hellos_get(client):
    service.context = {}
    name = escape(_.TEST_NAME)
    try:
        response = client.get(f"{_.BASE_URL}/{name}")
        assert 404 == response.status_code
    except werkzeug.exceptions.NotFound as eNotFound:
        pass

    response = client.post(_.BASE_URL, json={"name": name})
    assert 201 == response.status_code

    response = client.get(f"{_.BASE_URL}/{name}")
    assert 200 == response.status_code
    assert response.is_json
    assert response.json["message"] == f"Hello {name}"


def test_hellos_post(client):
    service.context = {}
    name = escape(_.TEST_NAME)

    response = client.post(
        _.BASE_URL,
        json={
            "name": name,
        },
    )
    assert 201 == response.status_code
    assert response.is_json
    assert response.json == {
        "message": f"Hello {name}",
    }

    try:
        response = client.post(
            _.BASE_URL,
            json={
                "name": name,
            },
        )
        assert 409 == response.status_code
    except werkzeug.exceptions.Conflict as eConflict:
        pass


def test_hellos_delete(client):
    service.context = {}
    name = escape(_.TEST_NAME)

    response = client.delete(name)
    assert 404 == response.status_code

    response = client.post(
        _.BASE_URL,
        json={
            "name": name,
        },
    )
    assert 201 == response.status_code
    assert response.is_json
    assert response.json == {
        "message": f"Hello {name}",
    }

    name_url = escape(_.TEST_NAME)
    response = client.delete(f"{_.BASE_URL}/{name_url}")
    assert 204 == response.status_code

    response = client.delete(name)
    assert 404 == response.status_code


def test_hellos_list(client):
    service.context = {}
    name = escape(_.TEST_NAME)

    response = client.get(_.BASE_URL)
    assert 200 == response.status_code
    assert response.is_json
    assert response.json == []

    response = client.post(
        _.BASE_URL,
        json={
            "name": name,
        },
    )
    assert 201 == response.status_code
    assert response.is_json
    assert response.json == {
        "message": f"Hello {name}",
    }
    response = client.get(_.BASE_URL)
    assert 200 == response.status_code
    assert response.is_json
    assert response.json == [name]

    name_url = escape(_.TEST_NAME)
    response = client.delete(f"{_.BASE_URL}/{name_url}")
    assert 204 == response.status_code
    response = client.get(_.BASE_URL)
    assert 200 == response.status_code
    assert response.is_json
    assert response.json == []
