import unittest

class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("*#"*40)
        print("Class 1 -> Class Level setUp")
        print("*#" * 40)

    def setUp(self):
        print("Class 1 -> setUp")

    def test_class1_methodA(self):
        print("Running class 1 -> method A")

    def test_class1_methodB(self):
        print("Running class 1 -> method B")

    def tearDown(self):
        print("Class 1 -> tearDown")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 40)
        print("Class 1 -> Class Level tearDown")
        print("*#" * 40)

if __name__ == '__main__':
    unittest.main(verbosity=2)

