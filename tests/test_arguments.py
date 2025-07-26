#!/usr/bin/env python3

from my_service.arguments import parser, parse


def test_parser():
    parser()


def test_parse():
    result = parse(parser(), args=["--verbose"])
    assert result.is_verbose

    result = parse(parser(), args=[])
    assert not result.is_verbose

    result = parse(parser(), args=["--debug"])
    assert result.is_debug

    result = parse(parser(), args=[])
    assert not result.is_debug
