#!/usr/bin/env python3
"""Hello world package"""
from flask import Flask, abort, Blueprint


class _:
    METHOD_GET = "GET"
    METHOD_POST = "POST"
    METHOD_PUT = "PUT"
    METHOD_PATCH = "PATCH"
    METHOD_DELETE = "DELETE"

    RES_HELLOS = "hellos"

    ROUTE_HELLO = "/" + RES_HELLOS
    ROUTE_HELLO_GET = ROUTE_HELLO + "/<name>"
    ROUTE_HELLO_LIST = ROUTE_HELLO
    ROUTE_HELLO_CREATE = ROUTE_HELLO
    ROUTE_HELLO_DELETE = ROUTE_HELLO + "/<name>"


# Create blueprint hellos
hellos_bp = Blueprint("hellos", __name__)


class hellos:
    def __init__(self):
        self.context = {
            _.RES_HELLOS: {},
        }

    @hellos_bp.route(_.ROUTE_HELLO_GET, methods=[_.METHOD_GET])
    def get_hellos(self, name):
        """Return message for key 'name'

        Args:
            name (str) is the name of a previous POST resource.
        Return:
            (str) json with message filled with "Hello <name>"
        """
        if not name in self.context[_.RES_HELLOS]:
            abort(404)
        response = {
            "message": "Hello {}".format(name),
        }
        return response, 200

    @hellos_bp.route(_.ROUTE_HELLO_LIST, methods=[_.METHOD_GET])
    def list_hellos(self):
        """List the current available keys

        Return:
            (str) json with an array of keys.
        """
        response = self.context[_.RES_HELLOS].keys()
        return response, 200

    @hellos_bp.route(_.ROUTE_HELLO_DELETE, methods=[_.METHOD_DELETE])
    def delete_hellos(self, name):
        """Delete an existing key

        Args:
            name (str) the key to be deleted.
        """
        if not name in self.context[_.RES_HELLOS]:
            abort(404, description="name={} not found".format(name))
        response = None
        return response, 204

    @hellos_bp.route(_.ROUTE_HELLO_CREATE, methods=[_.METHOD_POST])
    def post_hellos(self, name):
        """Create a new key if it does not exist.

        Args:
            name (str) the key to create.
        Return:
            A json with "message" equals to "Hello <name>".
        """
        if name in self.context[_.RES_HELLOS]:
            abort(409, description="name={} already exists".format(name))
        self.context[_.RES_HELLOS][name] = 1
        response = {
            "message": "Hello {}".format(name),
        }
        return response, 201
