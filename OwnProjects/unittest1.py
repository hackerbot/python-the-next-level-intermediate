# https://www.youtube.com/watch?v=BXHzjgafeAg

from __future__ import print_function
import unittest

def ExponentCalc(x,y):
    return x ** y

print(ExponentCalc(5,4))

class ExponentCalcTest(unittest.TestCase):
    def testSuccess(self):
        msg = 'Test Error'
        result = ExponentCalc(5,4)
        self.assertEqual(result, 624, msg)
    
    def testFailure(self):
        msg = 'Test Failure Error'
        result = ExponentCalc(3,8)
        self.assertEqual(result, 6560, msg)

unittest.main()