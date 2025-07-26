#!/usr/bin/env python3

import werkzeug
import my_service.service as service


def test_not_found():
    service.not_found(werkzeug.exceptions.NotFound("not found"))
