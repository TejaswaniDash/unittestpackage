"""
* Test Fixture- setup and tear down method; preparation method ; prerequisite , and clean up before and after test
* Test Case-
# smallest unit of testing in unittest module,
# checks for a response to a particular set of actions using the assert methods.

* Test Suite-
# Collection of multiple test case. aka group of test case
# they can be variety of class and then we group them together to run them in the single execution.

* Test Runner- responsible for execution of tests, and provide results to the user.
* Test Report- displays the summary of test results, and kind of shows the pass and fail status of the executed test cases.


* All these help to create a flow to test the application
"""
"""
# CREATION OF THE TEST CASE

"""

import unittest

class TestClassDemo(unittest.TestCase):
    #here we are inheriting the test case from unittest
    #once we inherit this we will have all the functionality provided by the class into our class

#Create a setUp method
    def setUp(self):
        print("I will run once before each test")
# starting point for a TestCase class is the setUp method,
# and this one we can use to perform some tasks at the start of each test.
# This will execute every time before each test method starts.
# the content inside this, they can be prerequisites,
# such as loading test data, opening log files,
# In case of testing a web application, then it could be creating an instance of the browser driver, navigating to the base page,
# no argument and doesn't return anything

    def test_methodA(self):
        print("Rrunning method A")

    def test_methodB(self):
        print("Rrunning method B")
# important that we name these methods beginning with the word 'test'.
# This is the naming convention that is going to inform the test runner that this method is a test,
# and then only test method understands that this is a test method, and I need to treat it as a test.

# Clean up whatever we setUp

    def tearDown(self):
        print("I will run once after each test")
# this tearDown method is used to clean up any initialized values after the test is executed
# Clean up the valuses initiallize by setUp method when we run the test case

# RUN THE UNITTEST

if __name__ == '__main__':
    unittest.main(verbosity=2)

