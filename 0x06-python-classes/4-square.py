#!/usr/bin/python3
"""Define class square"""


class Square:
    """Initialize a square object"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif type(size) is int and size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is int and size >= 0:
            self.__size = size
    
    """Returns the area of the square"""
    def area(self):
        if type(self.__size) is int:
            return self.__size ** 2
    
    """Returns the size of the square"""
    @property
    def size(self):
        return self.__size

    """Setting the value of the size of the square"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif type(value) is int and value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) is int and value >= 0:
            self.__size = value
