#!/usr/bin/python3
"""define class Square"""


class Square:
    """Defines a square:"""

    def __init__(self, size=0):
        """Initializer object"""

        self.__size = size

    def area(self):
        """return area of the Square in the atribute private __size"""

        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print a square with self.__size"""

        if self.__size == 0:
            print("\n", end="")
        else:
            [print('#' * self.__size) for i in range(self.__size)]
