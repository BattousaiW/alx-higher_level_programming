#!/usr/bin/python3
"""Define an inherits_from class"""


def inherits_from(obj, a_class):

    """function to check if obj is inherited from a class
    Arguments:
        param1: obj
        param2: a_class that matches the obj
    Return:
    True for issubclass of obj or False if not
    """

<<<<<<< HEAD
    return isinstance(obj, a_class)
=======
    return issubclass(type(obj), a_class) and (type(obj) != a_class)
>>>>>>> 9fc2b5ae0f0fd7c8635afa0885c44320ef38b6d5
