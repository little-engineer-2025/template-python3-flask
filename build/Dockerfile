FROM docker.io/library/python:3.13.5
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY . .
RUN pip3 install poetry \
    && poetry install
# TODO Uncomment and update the port where your app listen
# EXPORT 4000
CMD ["/bin/bash", "-c", "$(poetry env activate); exec /usr/bin/env python3 -m my_service \"$@\""]
