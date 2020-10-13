from models.square import Square
import unittest
import inspect
import pep8


class TestsSquare(unittest.TestCase):
    """test class for square"""

    def test_docstring(self):
        """ check for docstring in base"""
        self.assertTrue(len(Square.__doc__.strip()) > 0)
        functions = inspect.getmembers(Square, predicate=inspect.ismethod)
        for name, func in functions:
            self.assertTrue(len(name.__doc__.strip()) > 0)

    def test_pep8(self):
        """
        Test for PEP-8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0)

    def test_square_validate_attributes(self):
        """test for the validation cases for the input arguments"""
        self.assertRaises(ValueError, Square, 0, 50)
        self.assertRaises(TypeError, Square, "A", 20)
        self.assertRaises(TypeError, Square, 2.5, 20)
        self.assertRaises(ValueError, Square, -5, 10)
        p5 = Square(9)
        with self.assertRaises(ValueError):
            p5.size = 0
        with self.assertRaises(ValueError):
            p5.size = -10
        with self.assertRaises(ValueError):
            p5.x = -1
        with self.assertRaises(ValueError):
            p5.y = -3
        with self.assertRaises(TypeError):
            p5.size = 1.5
        with self.assertRaises(TypeError):
            p5.x = 1.5
        with self.assertRaises(TypeError):
            p5.y = 1.5
        with self.assertRaises(TypeError):
            p5.size = "Holberton"
        with self.assertRaises(TypeError):
            p5.x = "Holberton"
        with self.assertRaises(TypeError):
            p5.y = "Holberton"

    def test_rectangle_update(self):
        """test for update method"""
        with self.assertRaises(ValueError):
            Square(5).update(1, 0, 3, 5)
        with self.assertRaises(ValueError):
            Square(5).update(1, -10, 3, 5)
        with self.assertRaises(ValueError):
            Square(5).update(1, 8, -1, 5)
        with self.assertRaises(ValueError):
            Square(5).update(1, 8, 3, -3)
        with self.assertRaises(TypeError):
            Square(5).update(1, 1.5, 3, 5)
        with self.assertRaises(TypeError):
            Square(5).update(1, 8, 1.5, 5)
        with self.assertRaises(TypeError):
            Square(5).update(1, 8, 3, 1.5)
        with self.assertRaises(NameError):
            Square(5).update(1, "height", 3, 5)
        with self.assertRaises(NameError):
            Square(5).update(1, 8, "Holberton", 5)
        with self.assertRaises(NameError):
            Square(5).update(1, 8, 3, "School")
        with self.assertRaises(TypeError):
            Square(5).update(1,[1.5, 2], 3, 5)
        with self.assertRaises(TypeError):
            Square(5).update(1, (2, 3), 3, 5)
        with self.assertRaises(TypeError):
            Square(5).update(1, 8, [1, 2, 3], 5)
        with self.assertRaises(TypeError):
            Square(5).update(1, 8, 3, (2, 3))

        r1 = Square(5, 0, 0, 12)
        r1.update( 15, 1, 2, 122)
        self.assertEqual(r1.id, 15)
        self.assertEqual(r1.size, 1)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 122)

    def test_rectangle_update_2(self):
        """test for kwargs argumets"""
        #test the functionality of aal the validation
        with self.assertRaises(ValueError):
            Square(5).update(id=1, size=0, x=3, y=5)
        with self.assertRaises(ValueError):
            Square(5).update(id=1, size=-10, x=3, y=5)
        with self.assertRaises(ValueError):
            Square(5).update(id=1, size=8, x=-1, y=5)
        with self.assertRaises(ValueError):
            Square(5).update(id=1, size=8, x=3, y=-3)
        with self.assertRaises(TypeError):
            Square(5).update(id=1, size=2.3, x=3, y=5)
        with self.assertRaises(TypeError):
            Square(5).update(id=1, size=8, x=1.5, y=5)
        with self.assertRaises(TypeError):
            Square(5).update(id=1, size=8, x=3, y=1.5)
        with self.assertRaises(NameError):
            Square(5).update(id=1, size="height", x=3, y=5)
        with self.assertRaises(NameError):
            Square(5).update(id=1, size=8, x="Holberton", y=5)
        with self.assertRaises(NameError):
            Square(5).update(id=1, size=8, x=3, y="School")
        with self.assertRaises(TypeError):
            Square(5).update(id=1, size=[1.5, 2], x=3, y=5)
        with self.assertRaises(TypeError):
            Square(5).update(id=1, size=(2, 3), x= 3, y=5)
        with self.assertRaises(TypeError):
            Square(5).update(id=1, size=8, x=[1, 2, 3], y=5)
        with self.assertRaises(TypeError):
            Square(5).update(id=1, size=8, y=[1, 2, 3], x=5)
        #test if kwargs are being assigned correctly
        r1 = Square(5, 0, 0, 12)
        r1.update( id=15, size=15, x=2, y=122)
        self.assertEqual(r1.id, 15)
        self.assertEqual(r1.size, 15)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 122)
        #test if arguments are not ordered everything is assigned right way
        r1 = Square(5, 0, 0, 12)
        r1.update(y=15, id=15, size=2, x=122)
        self.assertEqual(r1.id, 15)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 122)
        self.assertEqual(r1.y, 15)

        #test if args exist kwargs are not assigned
        r1 = Square(5, 0, 0, 12)
        r1.update(id=15 , height=1, x=2, y=122, z=60)
        with self.assertRaises(AttributeError):
            self.assertFalse(r1.z)

    def test_square_size(self):

        r1 = Square(5)
        with self.assertRaises(ValueError):
            r1.size = 0
        with self.assertRaises(ValueError):
            r1.size = -5
        self.assertEqual(r1.size, 5)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 5)
        with self.assertRaises(TypeError):
            r1.size = [1, 2, 3]
        with self.assertRaises(TypeError):
            r1.size = "holberton"

    def test_square_dict_repr(self):
        pass
