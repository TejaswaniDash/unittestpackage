"""
HOW TO IMPEMENT CLASS LEVEL SetUp AND TearDown METHODS

* Here, we want something that executes once and then all these three,
all these flow will go on, then we want a tearDown that will execute only once.
"""


import unittest

class TestClassDemo2(unittest.TestCase):


    @classmethod  # used decorators
    def setUpClass(cls):
        print("*#"*40)
        print("I will run only once before all tests")
        print("*#" * 40)

    def setUp(self):
        print("I will run once before every test")

    def test_methodA(self):
        print("Rrunning method A")

    def test_methodB(self):
        print("Rrunning method B")

    def tearDown(self):
        print("I will run once after each test")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 40)
        print("I will run only once after all tests")
        print("*#" * 40)


if __name__ == '__main__':
    unittest.main(verbosity=2)

