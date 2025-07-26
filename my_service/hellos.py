#!/usr/bin/env python3
"""Hello world package"""
from flask import abort, Blueprint, request


# pylint: disable=too-few-public-methods
class _:
    METHOD_GET = "GET"
    METHOD_POST = "POST"
    METHOD_PUT = "PUT"
    METHOD_PATCH = "PATCH"
    METHOD_DELETE = "DELETE"

    RES_HELLOS = "hellos"

    ROUTE_HELLOS = "/" + RES_HELLOS
    ROUTE_HELLOS_LIST = ROUTE_HELLOS
    ROUTE_HELLOS_GET = ROUTE_HELLOS + "/<name>"
    ROUTE_HELLOS_CREATE = ROUTE_HELLOS
    ROUTE_HELLOS_DELETE = ROUTE_HELLOS + "/<name>"


context = {}
bp = Blueprint("hellos", __name__)


@bp.route(_.ROUTE_HELLOS_GET, methods=[_.METHOD_GET])
def get(name):
    """Return message for key 'name'

    Args:
        name (str) is the name of a previous POST resource.
    Return:
        (str) json with message filled with "Hello <name>"
    """
    if not name in context:
        abort(404)
    response = {
        "message": f"Hello {name}",
    }
    return response, 200


@bp.route(_.ROUTE_HELLOS_LIST, methods=[_.METHOD_GET])
def list_collection():
    """List the current available keys

    Return:
        (str) json with an array of keys.
    """
    response = list(context.keys())
    return response, 200


@bp.route(_.ROUTE_HELLOS_DELETE, methods=[_.METHOD_DELETE])
def delete(name):
    """Delete an existing key

    Args:
        name (str) the key to be deleted.
    """
    if not name in context:
        abort(404, description=f"name={name} not found")
    del context[name]
    return "", 204


@bp.route(_.ROUTE_HELLOS_CREATE, methods=[_.METHOD_POST])
def post():
    """Create a new key if it does not exist.

    Args:
        name (str) the key to create.
    Return:
        A json with "message" equals to "Hello <name>".
    """
    assert request.is_json
    name = request.json["name"]
    if name in context:
        abort(409, description=f"name={name} already exists")
    context[name] = {}
    response = {
        "message": f"Hello {name}",
    }
    return response, 201
