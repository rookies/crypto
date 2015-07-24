#!/usr/bin/python
from Primes import Generators
from Primes import Tests
import Primes
import unittest

class GeneratorsTest(unittest.TestCase):
	def testSimpleGenerator(self): ##FIXME##
		self.assertEqual(Generators.simpleGenerator(1, 200), Primes.primes[:46])

class TestsTest(unittest.TestCase):
	def testSimpleTest(self): ##TODO##
		pass
