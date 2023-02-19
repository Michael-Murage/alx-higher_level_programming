#!/usr/bin/python3
"""Define class square"""


class Square:
    __size = 0
    """Initialize a square object"""
    def __init__(self, inp=0):
        if type(inp) is not int:
            raise TypeError("size must be an integer")
            return
        if type(inp) is int and inp < 0:
            raise ValueError("size must be >= 0")
            return
        if type(inp) is int and inp >= 0:
            self.__size = inp
