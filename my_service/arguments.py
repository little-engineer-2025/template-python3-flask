# see: https://docs.python.org/3/library/argparse.html

"""
Configure the arguments accepted by your script.
"""
import sys
import argparse


def parser():
    """parser Configure the argument parser and return it"""
    p = argparse.ArgumentParser()
    p.add_argument(
        "--verbose", action="store_true", dest="is_verbose", help="Verbose logs"
    )
    p.add_argument("--debug", action="store_true", dest="is_debug", help="Debug logs")
    return p


def parse(the_parser, args=sys.argv[1:]):
    """Retrieve a new argument parser and extract the arguments"""
    result = the_parser.parse_args(args=args)
    return result
