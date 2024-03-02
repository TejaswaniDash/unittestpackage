"""
HOW TO COMBINE TWO PYTHON FILE TEST CLASS CASES AND RUN TEST SUITE

* how do we run the multiple test cases together?
* how do we achieve grouping of the test cases in a test suite, and then when we run a test suite,
  it should run all the test classes that we want to.

"""


import unittest

from unittestpackage.test_class1 import TestClass1
from unittestpackage.test_class2 import TestClass2

#get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)
#load all the test from test_class1 & 2 to TC1 and TC2 respectively.
#Create a test suite combining TestClass1 and TestClass2

smoke_test = unittest.TestSuite([tc1,tc2])

#trigger the run

unittest.TextTestRunner(verbosity=2).run(smoke_test)
