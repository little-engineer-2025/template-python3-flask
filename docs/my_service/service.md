Module my_service.service
=========================
Hello world package

Functions
---------

`healthz()`
:   Service liveness
    
    Return:
        200 if the service is live.
        500 if the service is is not alive.

`not_found(error)`
:   Default 404 error handler

`prometheus()`
:   TODO Add prometheus handler to return metrics.

`readyz()`
:   Service readiness
    
    Return:
        200 if the service is ready to attend requests.
        500 if the service is is not ready to attend requests.