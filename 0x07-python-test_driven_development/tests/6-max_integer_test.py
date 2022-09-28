#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_integer_list_integers(self):
        integers = [1, 2, 3, 4]
        self.assertEqual(max_integer(integers), 4)

        integers1 = [1, 4, 3, 2]
        self.assertEqual(max_integer(integers1), 4)

    def test_exceptions(self):
        # checks for mismatching number of argument
        with self.assertRaises(TypeError):
            max_integer()

            integers = [1, 2, 4, 3]
            max_integer(integers, 'what')

        # checks for mismatching type
        with self.assertRaises(TypeError):
            integers = [-1, -2, False, -4]
            max_integer(integers)
        with self.assertRaises(TypeError):
            integers = [-1, -2, True, -4]
            max_integer(integers)

        with self.assertRaises(TypeError):
            integers = [1, 2, None, 4]
            max_integer(integers)

        with self.assertRaises(TypeError):
            integers = [1, '2', 3, 4]
            max_integer(integers)

        with self.assertRaises(TypeError):
            integers = [1, 2, 3.14, 4]
            max_integer(integers)

        with self.assertRaises(TypeError):
            integers = [1, 2, (3+5j), 4]
            max_integer(integers)


if __name__ == '__main__':
    unittest.main()
