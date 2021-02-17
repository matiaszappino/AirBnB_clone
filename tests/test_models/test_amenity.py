#!/usr/bin/python3
"""Tests File"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """Test of Amenity class"""

    def test_Amenity(self):
        """Test instance of amenity class"""
        new = Amenity()
        new2 = Amenity()
        strmethod = "[{}] ({}) {}".format(new.__class__.__name__,
                                          new.id, new.__dict__)
        self.assertIsInstance(new, BaseModel)
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        self.assertEqual(issubclass(new.__class__, BaseModel), True)
        self.assertIs(type(new), Amenity)
        self.assertTrue(hasattr(new, "id"))
        self.assertEqual(new.__str__(), strmethod)
        self.assertEqual(type(new.id), str)

    def test_attr(self):
        """Test attributes of the class"""
        new = Amenity()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))

    def test_documentation(self):
        """Check documentation"""
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)


if __name__ == "__main__":
    unittest.main()
