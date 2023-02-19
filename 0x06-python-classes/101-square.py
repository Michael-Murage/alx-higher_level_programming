#!/usr/bin/python3
"""Define class square"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square object"""

        self.__size = size
        self.__position = position

    def area(self):
        """Returns the area of the square"""
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
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Printd the square"""

        print(self)

    def __str__(self):
        """Printable representation of the square"""

        to_print = ""
        if self.__size == 0:
            return to_print
        for i in range((self.__position)[1]):
            to_print = to_print + "\n"
        for j in range(self.__size):
            for k in range((self.__position)[0]):
                to_print = to_print + " "
            for j in range(self.size):
                to_print = to_print + "#"
            to_print = to_print + "\n"
        return to_print[:-1]

    @property
    def position(self):
        """Returns the position attribute"""

        return self.__position

    @position.setter
    def position(self, value):
        if len(value) == 2 and all(isinstance(i, int) for i in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
