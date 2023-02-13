#!/usr/bin/python3
"""Defines classes for models/base_model.py. """
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import uuid


class BaseModelTest(unittest.TestCase):
    """ test case class for BaseModel class """
    def test_init(self):
        """ testing __init__ method """
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "__class__"))
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))

    def test_init_with_args(self):
        """ testing __init__ method when args are given """
        test_dict = {'__class__': 'BaseModel',
                     'id': '8920ee99-8e15-4d4a-b88a-37c883ac6eb1',
                     'created_at': "2017-01-15 12:00:00.000000",
                     'updated_at': "2017-01-16 12:00:00.000000"}

        bm = BaseModel(test_dict)
        bm.save()
        self.assertTrue(hasattr(bm, 'updated_at'))
        self.assertEqual(bm.id, test_dict['id'])
        self.assertEqual(bm.created_at, test_dict['created_at'])
        self.assertEqual(bm.updated_at, test_dict['updated_at'])
        self.assertTrue(type(bm.created_at), type(test_dict['created_at']))

    def test_save(self):
        """ testing save method """
        bm = BaseModel()
        self.assertTrue(hasattr(bm, 'updated_at'))
        bm.save()
        self.assertTrue(hasattr(bm, 'updated_at'))

    def test_to_dict(self):
        """ testing to_json method """
        bm = BaseModel()
        jsoned_bm = bm.to_dict()
        self.assertTrue(type(jsoned_bm) is dict)


if __name__ == '__main__':
    unittest.main()
