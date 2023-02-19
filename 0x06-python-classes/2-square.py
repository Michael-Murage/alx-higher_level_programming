#!/usr/bin/python
class Square:
    __size = 0
    def __init__(self, inp=0):
        if type(inp) is not int:
            raise TypeError("size must be an integer")
            return
        if type(inp) is int and inp < 0:
            raise ValueError("size must be >= 0")
            return
        if type(inp) is int and inp >= 0:
            self.__size = inp
