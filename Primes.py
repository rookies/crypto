#!/usr/bin/python

primes = [
	    2,    3,    5,    7,   11,   13,   17,   19,   23,   29,
	   31,   37,   41,   43,   47,   53,   59,   61,   67,   71,
	   73,   79,   83,   89,   97,  101,  103,  107,  109,  113,
	  127,  131,  137,  139,  149,  151,  157,  163,  167,  173,
	  179,  181,  191,  193,  197,  199,  211,  223,  227,  229,
	  233,  239,  241,  251,  257,  263,  269,  271,  277
]

class Tests(object):
	@staticmethod
	def simpleTest(n): ##FIXME##
		if n == 1:
			return False
		for i in range(2, int(n/2)+1):
			if (n % i) == 0:
				return False
		return True

class Generators(object):
	@staticmethod
	def simpleGenerator(lower, upper, test=Tests.simpleTest): ##FIXME##
		res = []
		for n in range(lower, upper+1):
			if test(n):
				res.append(n)
		return res
