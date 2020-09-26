#!/usr/bin/python3
""" Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_end(self):
        """Check output for normal input"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_begin(self):
        """Check output for normal input"""
        self.assertEqual(max_integer([100, 50, 1, 68]), 100)

    def test_max_middle_neg(self):
        """Check output for normal input"""
        _list = [-1, 8, 5]
        self.assertEqual(max_integer(_list), 8)

    def test_max_at_middle(self):
        """Check output for normal input"""
        self.assertEqual(max_integer([98, 115, 3]), 115)

    def test_max_neg(self):
        """Check output for normal input"""
        self.assertEqual(max_integer([-1, -5, -8]), -1)

    def test_max_at_one(self):
        """Check output for normal input"""
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
