#!/usr/bin/python3
"""Define class square"""


class Square:
    def __init__(self, size=0):
        """Initialize a square object"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif type(size) is int and size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is int and size >= 0:
            self.__size = size
    
    def area(self):
        """Returns the area of the square"""

        if type(self.__size) is int:
            return self.__size ** 2
    
    @property
    def size(self):
        """Returns the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setting the value of the size of the square"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif type(value) is int and value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) is int and value >= 0:
            self.__size = value

    def my_print(self):
        """Prints to stdout the square with the character #"""
        
        if self.__size == 0:
            print("\n", end="")
        else:
            for i in range(self.__size):
                print('#' * self.__size)
