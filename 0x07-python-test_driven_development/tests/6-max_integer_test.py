#!/usr/bin/python3
""" Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

   def regular_cases(self):
        """Check for regular inputs"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([50, 100, 1, -8]), 100)
        self.assertEqual(max_integer([-1, -10, -3]), -1)

    def check_empty(self):
        """Check for an empty list"""
        self.assertIsNone(max_integer([]))

    def check_tuple(self):
        """Check for different types of input"""
        self.assertEqual(max_integer((2, 3)), 3)

    def check_None(self):
        """Check for different types of input"""
        self.assertIsNone(max_integer(None))

    def test_float(self):
        """Check for floats"""
        _list = [1.5, 2.4, 3.5, 4.1]
        self.assertEqual(max_integer(_list), 4.1)

    def test_docstringmod(self):
        """Check docstring for module"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(m is not None and len(m) > 0)

    def test_docstringfunc(self):
        f = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(f is not None and len(f) > 5)

    def test_morethan(self):
        # check that max_integer fails when you pass more than one argument
        with self.assertRaises(TypeError):
            _max = max_integer(1, 1)


if __name__ == '__main__':
    unittest.main()
