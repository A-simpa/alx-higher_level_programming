#!/usr/bin/python3
""" we define a square class with one attribute
size which is peculiar to different sqaure object.
size is always be an integer greater than or equal to 0

Attribute:
    size; size tells the size of the sides of the square


Method:
    area; calculates the are of the square
    my_print; print the square as a grid of hashes
"""


class Square:
    """This class initializes an attribute size on each instance
    using the init function, condition to set size
    """
    def __init__(self, size=0):
        self.size = size

    """ This is the method used to get class attribute size"""
    @property
    def size(self):
        return self.__size

    """This is the method used to set the class attribute size"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ The method to get the area of the square"""

    def area(self):
        return (self.__size * self.__size)

    """  This method prints the square object
         0, size means no square """

    def my_print(self):
        if self.__size != 0:
            for line in range(self.__size):
                print("#" * self.__size)
        else:
            print("")
