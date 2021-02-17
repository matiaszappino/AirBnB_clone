#!/usr/bin/python3
"""Tests File"""
import unittest
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):
    """Test of Review class"""

    def test_Review(self):
        """Test instance of amenity class"""
        new = Review()
        new2 = Review()
        self.assertIsInstance(new, BaseModel)
        self.assertEqual(issubclass(new.__class__, BaseModel), True)
        self.assertIs(type(new), Review)
        self.assertTrue(hasattr(new, "id"))
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertEqual(type(new.id), str)

    def test_attr(self):
        """Test attributes of the instance"""
        new = Review()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "place_id"))
        self.assertTrue(hasattr(new, "user_id"))
        self.assertTrue(hasattr(new, "text"))
        self.assertNotEqual(type(new.place_id), int)
        self.assertNotEqual(type(new.place_id), list)
        self.assertEqual(type(new.place_id), str)
        self.assertNotEqual(type(new.user_id), list)
        self.assertNotEqual(type(new.user_id), int)
        self.assertEqual(type(new.user_id), str)
        self.assertNotEqual(type(new.text), list)
        self.assertNotEqual(type(new.text), int)
        self.assertEqual(type(new.text), str)

    def test_documentation(self):
        """Check documentation"""
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)


if __name__ == "__main__":
    unittest.main()
