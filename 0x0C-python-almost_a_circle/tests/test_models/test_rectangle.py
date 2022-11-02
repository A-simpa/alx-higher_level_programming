#!/usr/bin/python3
""" defines test for the triangle class"""


import io
import sys
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle


class TriangleTestCases(TestCase):
    """ the test cases for the triangle classes as a method """

    def test_instance_of_base(self):
        """ test if instances are instance of Base and Rectangle"""
        self.assertIsInstance(Rectangle(2, 3), Base)

    def test_instance_of_rectangle(self):
        """ test if instance is an instance of rectange or base"""
        self.assertIsInstance(Rectangle(2, 3), Rectangle)

    def test_width_rigth(self):
        """ test if width is correct """
        t = Rectangle(2, 3)
        self.assertEqual(t.width, 2)

    def test_height_right(self):
        """ test if height is correct"""
        t = Rectangle(2, 3)
        self.assertEqual(t.height, 3)

    def test_id_multiple_none(self):
        """ test if id is set automatically"""
        r = Rectangle(4, 3, 4, 5)
        i = Rectangle(2, 1, 3, 5)
        self.assertEqual(i.id, r.id + 1)

    def test_width_type_error(self):
        """test to see if type error is raised"""
        with self.assertRaises(TypeError):
            Rectangle(2.5, 2)

    def test_width_value_error(self):
        """test to see if ValueError is raised"""
        with self.assertRaises(ValueError):
            Rectangle(-2, 1)

    def test_height_type_error(self):
        """test to see if typeError is raised"""
        with self.assertRaises(TypeError):
            Rectangle(2, 2.5)

    def test_width_type_error(self):
        """test to see if valueError is raised wrong width"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_x_type_error(self):
        """test for type error"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 2.5)

    def test_x_value_error(self):
        """test for x value error"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -2)

    def test_y_type_error(self):
        """test for correct y type"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 1, -2.5)

    def test_y_value_error(self):
        """test for correct y value"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 1, -2)

    def test_area(self):
        """test to see if area is correct"""
        t = Rectangle(1, 4)
        self.assertEqual(t.area(), 4)

    def test_display_with_hash(self):
        """test to see if display print expected output"""
        t = Rectangle(2, 3)
        capture_output = io.StringIO()
        sys.stdout = capture_output
        t.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capture_output.getvalue(), "##\n##\n##\n")

    def test_string(self):
        """test if the string representation is right"""
        t = Rectangle(1, 4, 3, 2, 12)
        self.assertEqual(str(t), "[Rectangle] (12) 3/2 - 1/4")
