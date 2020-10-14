#!/usr/bin/python3
"""Rectangle tests"""


from models.rectangle import Rectangle
from models.base import Base
import unittest
import inspect
import pep8
import io
import contextlib


class TestsRectangle(unittest.TestCase):
    """test class for rectangle"""
    def setUp(self):
        """Set up"""
        Base._Base__nb_objects = 0

    def test_rectangle_id(self):
        """Check for id."""
        r0 = Rectangle(1, 2)
        self.assertEqual(r0.id, 1)
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.id, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.id, 3)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(10, 2, 4, 5, 34)
        self.assertEqual(r4.id, 34)
        r5 = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(r5.id, -5)
        r6 = Rectangle(10, 2, 4, 5, 9)
        self.assertEqual(r6.id, 9)

    def tearDown(self):
        """Teardown"""
        pass

    def test_docstring(self):
        """ check for docstring in base"""
        self.assertTrue(len(Rectangle.__doc__.strip()) > 0)
        functions = inspect.getmembers(Rectangle, predicate=inspect.ismethod)
        for name, func in functions:
            self.assertTrue(len(name.__doc__.strip()) > 0)

    def test_pep8(self):
        """
        Test for PEP-8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0)

    def test_rectangle_inheritance(self):
        """Check for inheritance"""
        r1 = Rectangle(8, 2)
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_rectangle_validate_attributes(self):
        """test for the validation cases for the input arguments"""
        self.assertRaises(ValueError, Rectangle, 0, 50)
        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(TypeError, Rectangle, "A", 20)
        self.assertRaises(TypeError, Rectangle, 20, "N")
        self.assertRaises(TypeError, Rectangle, 2.5, 20)
        self.assertRaises(TypeError, Rectangle, 20, 8.5)
        self.assertRaises(ValueError, Rectangle, -5, 10)
        self.assertRaises(ValueError, Rectangle, 10, -8)
        self.assertRaises(ValueError, Rectangle, 0, 10)
        self.assertRaises(ValueError, Rectangle, 10, 0)
        p5 = Rectangle(9, 2)
        with self.assertRaises(ValueError):
            p5.width = 0
        with self.assertRaises(ValueError):
            p5.height = 0
        with self.assertRaises(ValueError):
            p5.width = -10
        with self.assertRaises(ValueError):
            p5.height = -8
        with self.assertRaises(ValueError):
            p5.x = -1
        with self.assertRaises(ValueError):
            p5.y = -3
        with self.assertRaises(TypeError):
            p5.height = 1.5
        with self.assertRaises(TypeError):
            p5.width = 2.3
        with self.assertRaises(TypeError):
            p5.x = 1.5
        with self.assertRaises(TypeError):
            p5.y = 1.5
        with self.assertRaises(TypeError):
            p5.height = "Holberton"
        with self.assertRaises(TypeError):
            p5.width = "School"
        with self.assertRaises(TypeError):
            p5.x = "Holberton"
        with self.assertRaises(TypeError):
            p5.y = "Holberton"

    def test_area_first(self):
        """test for the area method"""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
        with self.assertRaises(TypeError):
            Rectangle("A", 7, 0, 0, 35).area()
        with self.assertRaises(TypeError):
            Rectangle(8, "B", 0, 0, 35).area()
        with self.assertRaises(TypeError):
            Rectangle([], 7, 0, 0, 35).area()
        with self.assertRaises(TypeError):
            Rectangle(8, {}, 0, 0, 35).area()
        with self.assertRaises(TypeError):
            Rectangle(1.5, 7, 0, 0, 35).area()
        with self.assertRaises(TypeError):
            Rectangle(8, 8.3, 0, 0, 35).area()

    def test_rectangle_display(self):
        """test the display method"""
        f = io.StringIO()
        r1 = Rectangle(4, 5)
        with contextlib.redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        res = "####\n####\n####\n####\n####\n"
        self.assertEqual(s, res)

        #test for wrong arguments
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(9, 6)
            r1.display(9)
        self.assertEqual("display() takes 1 positional argument but 2 were given", str(x.exception))

        #test for x and y display
        f = io.StringIO()
        r1 = Rectangle(2, 3, 2, 2)
        with contextlib.redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        res = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, res)


    def test_rectangle_str(self):
        """test the overided method __str__"""
        pass

    def test_rectangle_update(self):
        """test for update method"""
        with self.assertRaises(ValueError):
            Rectangle(5,5).update(1, 0, 6, 3, 5)
        with self.assertRaises(ValueError):
            Rectangle(5,5).update(1, 8, 0, 3, 5)
        with self.assertRaises(ValueError):
            Rectangle(5,5).update(1, -10, 10, 3, 5)
        with self.assertRaises(ValueError):
            Rectangle(5,5).update(1, 10, -8, 3, 5)
        with self.assertRaises(ValueError):
            Rectangle(5,5).update(1, 8, 10, -1, 5)
        with self.assertRaises(ValueError):
            Rectangle(5,5).update(1, 8, 10, 3, -3)
        with self.assertRaises(TypeError):
            Rectangle(5,5).update(1, 8, 1.5, 3, 5)
        with self.assertRaises(TypeError):
            Rectangle(5,5).update(1, 2.3, 10, 3, 5)
        with self.assertRaises(TypeError):
            Rectangle(5,5).update(1, 8, 10, 1.5, 5)
        with self.assertRaises(TypeError):
            Rectangle(5,5).update(1, 8, 10, 3, 1.5)
        with self.assertRaises(NameError):
            Rectangle(5,5).update(1, 8, "height", 3, 5)
        with self.assertRaises(NameError):
            Rectangle(5,5).update(1, "school", 10, 3, 5)
        with self.assertRaises(NameError):
            Rectangle(5,5).update(1, 8, 10, "Holberton", 5)
        with self.assertRaises(NameError):
            Rectangle(5,5).update(1, 8, 10, 3, "School")
        with self.assertRaises(TypeError):
            Rectangle(5,5).update(1, 8, [1.5, 2], 3, 5)
        with self.assertRaises(TypeError):
            Rectangle(5,5).update(1, (2, 3), 10, 3, 5)
        with self.assertRaises(TypeError):
            Rectangle(5,5).update(1, 8, 10, [1, 2, 3], 5)
        r1 = Rectangle(5, 5, 0, 0, 12)
        r1.update( 15, 15 , 1, 2, 122)
        self.assertEqual(r1.id, 15)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 122)

    def test_rectangle_update_2(self):
        """test for kwargs argumets"""
        #test the functionality of aal the validation
        with self.assertRaises(ValueError):
            Rectangle(5,5).update(id=1, width=0, height=6, x=3, y=5)
        with self.assertRaises(ValueError):
            Rectangle(5,5).update(id=1, width=8, height=0, x=3, y=5)
        with self.assertRaises(ValueError):
            Rectangle(5,5).update(id=1, width=-10, height=10, x=3, y=5)
        with self.assertRaises(ValueError):
            Rectangle(5,5).update(id=1, width=10, height=-8, x=3, y=5)
        with self.assertRaises(ValueError):
            Rectangle(5,5).update(id=1, width=8, height=10, x=-1, y=5)
        with self.assertRaises(ValueError):
            Rectangle(5,5).update(id=1, width=8, height=10, x=3, y=-3)
        with self.assertRaises(TypeError):
            Rectangle(5,5).update(id=1, width=8, height=1.5, x=3, y=5)
        with self.assertRaises(TypeError):
            Rectangle(5,5).update(id=1, width=2.3, height=10, x=3, y=5)
        with self.assertRaises(TypeError):
            Rectangle(5,5).update(id=1, width=8, height=10, x=1.5, y=5)
        with self.assertRaises(TypeError):
            Rectangle(5,5).update(id=1, width=8, height=10, x=3, y=1.5)
        with self.assertRaises(NameError):
            Rectangle(5,5).update(id=1, width=8, height="height", x=3, y=5)
        with self.assertRaises(NameError):
            Rectangle(5,5).update(id=1, width="school", height=10, x=3, y=5)
        with self.assertRaises(NameError):
            Rectangle(5,5).update(id=1, width=8, height=10, x="Holberton", y=5)
        with self.assertRaises(NameError):
            Rectangle(5,5).update(id=1, width=8, height=10, x=3, y="School")
        with self.assertRaises(TypeError):
            Rectangle(5,5).update(id=1, width=8, height=[1.5, 2], x=3, y=5)
        with self.assertRaises(TypeError):
            Rectangle(5,5).update(id=1, width=(2, 3), height=10, x= 3, y=5)
        with self.assertRaises(TypeError):
            Rectangle(5,5).update(id=1, width=8, height=10, x=[1, 2, 3], y=5)
        #test if kwargs are being assigned correctly
        r1 = Rectangle(5, 5, 0, 0, 12)
        r1.update( id=15, width=15 , height=1, x=2, y=122)
        self.assertEqual(r1.id, 15)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 122)
        #test if arguments are not ordered everything is assigned right way
        r1 = Rectangle(5, 5, 0, 0, 12)
        r1.update(y=15, id=15 , height=1, width=2, x=122)
        self.assertEqual(r1.id, 15)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 122)
        self.assertEqual(r1.y, 15)

        #test if args exist kwargs are not assigned
        r1 = Rectangle(5, 5, 0, 0, 12)
        r1.update(id=15 , height=1, x=2, y=122, z=60)
        with self.assertRaises(AttributeError):
            self.assertFalse(r1.z)

    def test_rectangle_todictionary(self):
        """test to dictionary method"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(len(r1_dictionary), len(r_dictionary))
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(len(r1_dictionary), len(r2_dictionary))
        self.assertEqual(type(r2_dictionary), dict)
        self.assertFalse(r1 == r2)
        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(10, 2, 1, 9)
            r1_dictionary = r1.to_dictionary("Hi")
        self.assertEqual(s, str(x.exception))

if __name__ == '__main__':
    unittest.main()
