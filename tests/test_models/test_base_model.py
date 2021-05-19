#!/usr/bin/python3
"""test the airbnb project"""


import unittest
import uuid

from models.base_model import BaseModel
from datetime import datetime
#from models.base_model import Rectangle
# from models.square import Square

class TestClassMerthods(unittest.TestCase):
    """test the Airbnb project"""

    def test_BaseModel_id(self):
        self.assertEqual(type(BaseModel().id), str)

    def test_create_time(self):
        self.assertEqual(type(BaseModel().created_at), datetime)

    def test_save(self):
        nb = BaseModel()
        nb.save()
        t1 = nb.updated_at
        nb.save()
        t2 = nb.updated_at
        self.assertNotEqual(t1, t2)

    def test_to_dict(self):
        nb = BaseModel()
        self.assertEqual(type(nb.to_dict()), dict)


    def assertHasAttr(self):
        testBool = hasattr(BaseModel(), 'save()')
        self.assertTrue(testBool)









if __name__ == '__main__':
    unittest.main()

