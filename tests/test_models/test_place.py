#!/usr/bin/python3
"""test the airbnb project"""


import unittest
from models.place import Place


A = Place()


class TestClassMethods(unittest.TestCase):
    """test the Airbnb project"""

    def test_State_Place(self):
        self.assertEqual(type(A.city_id), str)
        self.assertEqual(type(A.user_id), str)
        self.assertEqual(type(A.name), str)
        self.assertEqual(type(A.description), str)
        self.assertEqual(type(A.number_rooms), int)
        self.assertEqual(type(A.number_bathrooms), int)
        self.assertEqual(type(A.max_guest), int)
        self.assertEqual(type(A.price_by_night), str)
        self.assertEqual(type(A.latitude), str)
        self.assertEqual(type(A.longitude), str)
        self.assertEqual(type(A.amenity_ids), str)