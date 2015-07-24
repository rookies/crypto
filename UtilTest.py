#!/usr/bin/python
from Util import Helpers
import Primes
import unittest

class HelpersTest(unittest.TestCase):
	__primeCount = 50
	
	def testParsePositiveInt(self):
		# Test for illegal values:
		try:
			Helpers.parsePositiveInt("abc")
		except ValueError:
			pass
		else:
			self.fail("Should raise ValueError when called with a non-number!")
		try:
			Helpers.parsePositiveInt(-5)
		except ValueError:
			pass
		else:
			self.fail("Should raise ValueError when called with a negative number!")
		try:
			Helpers.parsePositiveInt(0)
		except ValueError:
			pass
		else:
			self.fail("Should raise ValueError when called with zero!")
		# Test for legal values:
		testValues = { 5:5, 7.3:7, 7.9:7 }
		for val in testValues.items():
			self.assertEqual(Helpers.parsePositiveInt(val[0]), val[1])
		
	def testPrimeFactorization(self):
		testValues = { 1:[], 2:[(2,1)], 7:[(7,1)], 8:[(2,3)], 20:[(2,2),(5,1)], 436:[(2,2),(109,1)] }
		for val in testValues.items():
			self.assertEqual(Helpers.primeFactorization(val[0]), val[1], "Failed for n=%d" % val[0])
			
	def testPhiFunction(self):
		# Test for primes:
		for p in Primes.primes[:self.__primeCount]:
			self.assertEqual(Helpers.phiFunction(p), p-1, "Failed for n=p=%d" % p)
		# Test for products of 2 primes:
		for p in Primes.primes[:self.__primeCount]:
			for q in Primes.primes[:self.__primeCount]:
				if p != q:
					self.assertEqual(Helpers.phiFunction(p*q), (p-1)*(q-1), "Failed for n=p*q=%d*%d" % (p, q))
		# Test for other values:
		testValues = { 1:1, 8:4, 20:8, 436:216 }
		for val in testValues.items():
			self.assertEqual(Helpers.phiFunction(val[0]), val[1], "Failed for n=%d" % val[0])
			
	def testEuclidGCD(self):
		# Test for primes:
		for p in Primes.primes[:self.__primeCount]:
			for q in Primes.primes[:self.__primeCount]:
				self.assertEqual(Helpers.euclidGCD(p,q), (p if p == q else 1), "Failed for a=%d, b=%d" % (p,q))
		# Test for other values:
		testValues = { (7,30):1, (35,5):5 }
		for val in testValues.items():
			self.assertEqual(Helpers.euclidGCD(val[0][0], val[0][1]), val[1], "Failed for a=%d, b=%d" % val[0])
			
	def testPrimeFactorizedGCD(self):
		##TODO##
		pass
		
	def testHalfFactorizedGCD(self):
		##TODO##
		pass
