#!/usr/bin/python
from QuotientRing import Helpers
import unittest

class HelpersTest(unittest.TestCase):
	def testSquareAndMultiply(self): ##TODO##
		testValues = { (3,201,100):3 }
		for val in testValues.items():
			self.assertEqual(Helpers.squareAndMultiply(val[0][0], val[0][1], val[0][2]), val[1], "Failed for (b,e,n) = (%d,%d,%d)" % val[0])
