"""
HOW TO ASSERT TEST METHOD

unittest assert test-
https://docs.python.org/3/library/unittest.html#unittest.TestCase
"""
import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, " a is not true ")
        b = False
        self.assertFalse(b, " b is not true ")

    def test_assertEqual(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a, b, msg= " 'a' is not equal to 'b' ")



if __name__ == '__main__':
    unittest.main(verbosity=2)

"""
Failure Traceback
Example with negative values

* If the assertion fails at a line, it will not go to the next line in that particular test. 
* Instead, it will just come out and it will go to the next test method.
"""
# Failure Traceback
# Example with a assert False

import unittest

class AssertDemo2(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertFalse(a, " a is not false ")
        b = False
        self.assertFalse(b, " b is not true ")

    def test_assertEqual(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a, b, msg= " 'a' is not equal to 'b' ")



if __name__ == '__main__':
    unittest.main(verbosity=2)


# Example with b assert True
import unittest

class AssertDemo2(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, " a is not false ")
        b = False
        self.assertTrue(b, " b is not true ")

    def test_assertEqual(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a, b, msg= " 'a' is not equal to 'b' ")



if __name__ == '__main__':
    unittest.main(verbosity=2)

# Example with equal assert and b assert True

import unittest

class AssertDemo2(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, " a is not false ")
        b = False
        self.assertTrue(b, " b is not true ")

    def test_assertEqual(self):
        a = "Test"
        b = "test"
        self.assertEqual(a, b, msg= " 'a' is not equal to 'b' ")



if __name__ == '__main__':
    unittest.main(verbosity=2)


# Example with assert Not Equal

import unittest

class AssertDemo2(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, " a is not false ")
        b = False
        self.assertFalse(b, " b is not true ")

    def test_assertEqual(self):
        a = "Test"
        b = "test"
        self.assertNotEqual(a, b, msg= " 'a' is not equal to 'b' ")

if __name__ == '__main__':
    unittest.main(verbosity=2)
