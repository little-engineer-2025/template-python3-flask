Module my_service.hellos
========================
Hello world package

Functions
---------

`delete(name)`
:   Delete an existing key
    
    Args:
        name (str) the key to be deleted.

`get(name)`
:   Return message for key 'name'
    
    Args:
        name (str) is the name of a previous POST resource.
    Return:
        (str) json with message filled with "Hello <name>"

`list_collection()`
:   List the current available keys
    
    Return:
        (str) json with an array of keys.

`post()`
:   Create a new key if it does not exist.
    
    Args:
        name (str) the key to create.
    Return:
        A json with "message" equals to "Hello <name>".