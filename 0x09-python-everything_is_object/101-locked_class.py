#!/usr/bin/python3
"""Define a locked class."""


class LockedClass:
    """
    This class, LockedClass, is designed to restrict the dynamic creation
    of new instance attributes. Only the attribute 'first_name' is allowed.

    Attributes:
        __slots__ (list): A list containing only 'first_name', restricting
                         the creation of new attributes to this specific one.
    """

    __slots__ = ["first_name"]

