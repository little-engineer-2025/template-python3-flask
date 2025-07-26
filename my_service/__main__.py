#!/usr/bin/env python3

"""Run the hello function by default"""

from .service import app
from .arguments import parser, parse
from .logs import log_setup


def main():
    """entry point for your script."""
    args = parse(parser())
    log_setup(args)
    app.run(debug=True)


if __name__ == "__main__":
    main()
