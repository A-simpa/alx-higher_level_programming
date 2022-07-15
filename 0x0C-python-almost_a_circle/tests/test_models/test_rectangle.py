#!/usr/bin/python3
""" defines test for the triangle class"""


import os
from unittest import TestCase
from models.base import Base
from models.rectangle import Triangle


class TriangleTestCases(TestCase):
    """ the test cases for the triangle classes as a method """

    def test_instance(self):
        """ test if instances are instance of Base and Triangle"""

        t = Triangle(2, 3)
        self.assertIsInstance(t, Base)
        self.assertIsInstance(t, Triangle)

    def test_width_height(self):
        t = Triangle(2, 3)
        self.assertEqual(t.width, 2)
        self.assertEqual(t.height, 3)
        self.assertEqual(t.x, 0)
        self.assertEqual(t.y, 0)

    def test_all_arg(self):
        t = Triangle(2, 3, 4, 5, 3)
        self.assertEqual(t.width, 2)
        self.assertEqual(t.height, 3)
        self.assertEqual(t.x, 4)
        self.assertEqual(t.y, 5)

    def test_id_multiple_none(self):
        t = Triangle(2, 3, 4, 5)
        r = Triangle(4, 3, 4, 5)
        i = Triangle(2, 1, 3, 5)
        self.assertEqual(r.id, t.id + 1)
        self.assertEqual(i.id, r.id + 1)

if __name__ == 'main':
    unittest.main()
