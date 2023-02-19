#!/usr/bin/python3


class Square:
    """Define class square"""

    def __init__(self, size=0):
        """Initialize a square object"""
        self.size = size

    def area(self):
        """Returns the area of the square"""
        if type(self.__size) is int:
            return self.__size ** 2

    def __lt__(self, other):
        """Method for <"""
        if self.__size < other.__size:
            return True
        else:
            return False

    def __le__(self, other):
        """Method for <="""
        if self.__size <= other.__size:
            return True
        else:
            return False

    def __gt__(self, other):
        """Method for >"""
        if self.__size > other.__size:
            return True
        else:
            return False

    def __ge__(self, other):
        """Method for >="""
        if self.__size >= other.__size:
            return True
        else:
            return False

    def __eq__(self, other):
        """Method for =="""
        if self.__size == other.__size:
            return True
        else:
            return False

    def __ne__(self, other):
        """Method for !="""
        if self.__size != other.__size:
            return True
        else:
            return False

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the value of the size of the square"""
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
