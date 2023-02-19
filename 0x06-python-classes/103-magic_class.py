#!/usr/bin/python3

import math


class MagicClass:
    """Doc string"""
    def __init__(self, radius=0):
        """Doc string"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Doc String"""
        return (self.__radius) ** 2 * math.pi

    def circumference(self):
        """Doc string"""
        return math.pi * 2 * self.__radius
