#!/usr/bin/python3
"""Base test"""


from models.base import Base
from models.rectangle import Rectangle
import unittest
import inspect
import pep8


class TestBase(unittest.TestCase):
    """test class for base"""

    def test_docstring(self):
        """ check for docstring in base"""
        self.assertTrue(len(Base.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.ismethod)
        for name, func in functions:
            self.assertTrue(len(name.__doc__.strip()) > 0)

    def test_pep8(self):
        """
        Test for PEP-8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0)
 
    def test_base(self):
        """test simple funcionality of the root class"""

        p1 = Base()
        self.assertEqual(p1.id, 1)
        p2 = Base(2)
        self.assertEqual(p2.id, 2)
        p3 = Base()
        self.assertEqual(p3.id, 2)
        p4 = Base(None)
        self.assertEqual(p4.id, 3)

    def test_base_jsonstring(self):
        """test for json string method"""
        self.assertEqual(Base.to_json_string([]), [])
        self.assertEqual(Base.to_json_string(None), [])

if __name__ == '__main__':
    unittest.main()
