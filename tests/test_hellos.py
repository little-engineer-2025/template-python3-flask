#!/usr/bin/env python3

import os
import pytest
import werkzeug
import my_service.hellos as service


class _:
    TEST_NAME = "john doe"


def test_get_hellos(capsys):
    srv = service.Hellos()
    try:
        srv.get_hellos(_.TEST_NAME)
    except werkzeug.exceptions.NotFound as eNotFound:
        pass

    srv.post_hellos(_.TEST_NAME)
    response = srv.get_hellos(_.TEST_NAME)
    assert response[1] == 200
    assert len(response[0]) == 1
    assert response[0]["message"] == f"Hello {_.TEST_NAME}"


def test_post_hellos(capsys):
    srv = service.Hellos()
    srv.post_hellos(_.TEST_NAME)
    try:
        srv.post_hellos(_.TEST_NAME)
    except werkzeug.exceptions.Conflict as eConflict:
        pass


def test_delete_hellos():
    srv = service.Hellos()
    try:
        srv.delete_hellos(_.TEST_NAME)
    except werkzeug.exceptions.NotFound:
        pass

    srv.post_hellos(_.TEST_NAME)
    srv.delete_hellos(_.TEST_NAME)

    try:
        srv.delete_hellos(_.TEST_NAME)
    except werkzeug.exceptions.NotFound:
        pass


def test_list_hellos():
    srv = service.Hellos()
    srv.list_hellos()

    srv.post_hellos(_.TEST_NAME)
    srv.list_hellos()

    srv.delete_hellos(_.TEST_NAME)
    srv.list_hellos()
