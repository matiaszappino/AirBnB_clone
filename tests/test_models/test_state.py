#!/usr/bin/python3
"""Tests File"""
import unittest
from models.state import State
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):
    """Test of State class"""

    def test_State(self):
        """Test instance of amenity class"""
        new = State()
        new2 = State()
        self.assertIsInstance(new, BaseModel)
        self.assertEqual(issubclass(new.__class__, BaseModel), True)
        self.assertIs(type(new), State)
        self.assertTrue(hasattr(new, "id"))
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertEqual(type(new.id), str)

    def test_attr(self):
        """Test attributes of the instance"""
        new = State()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))
        self.assertFalse(hasattr(new, "state_id"))
        self.assertEqual(type(new.name), str)
        self.assertNotEqual(type(new.name), int)
        self.assertNotEqual(type(new.name), list)

    def test_documentation(self):
        """Check documentation"""
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)


if __name__ == "__main__":
    unittest.main()
