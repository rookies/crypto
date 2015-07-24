#!/usr/bin/python

class Helpers(object):
	@staticmethod
	def squareAndMultiply(b, e, n): ##FIXME##
		##TODO: Euler's theorem
		mask = 2**e.bit_length()
		hadFirstOne = False
		res = 1
		for i in range(e.bit_length(), -1, -1):
			if (e & mask) == 0:
				if hadFirstOne:
					res = (res**2) % n
			else:
				res = (res**2) % n
				res = (res*b) % n
				hadFirstOne = True
			mask >>= 1
		return res
