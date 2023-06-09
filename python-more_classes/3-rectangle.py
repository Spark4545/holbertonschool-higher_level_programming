#!/usr/bin/python3
"""
Module 2-rectangle
Contains class Rectangle
with private attribute width and height
"""


class Rectangle:
    """
    Defines class rectangle with private attribute width and height

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        def area(self)
        def perimeter(self)
        def __str__(self)
    """
    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns:
            width * height
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns:
            height * 2 + width * 2
        """
        if self.__height is 0 or self.__width is 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """
        print rectangle wuth #'s
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        rec = '\n'.join(['#' * self.__width for rows in range(self.__height)])
        return rec
