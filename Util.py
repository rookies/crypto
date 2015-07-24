#!/usr/bin/python
import Primes

class Helpers(object):
	@staticmethod
	def parsePositiveInt(n):
		n = int(n)
		if n <= 0:
			raise ValueError("This function only accepts positive numbers!")
		return n
		
	@staticmethod
	def primeFactorization(n):
		n = Helpers.parsePositiveInt(n)			
		tmp = {}
		for p in Primes.primes:
			while n % p == 0:
				n = int(n / p)
				if p in tmp:
					tmp[p] += 1
				else:
					tmp[p] = 1
		res = []
		for i in tmp.items():
			res.append(i)
		return res
		
	@staticmethod
	def phiFunction(n):
		primes = Helpers.primeFactorization(n)
		phi = 1
		for p in primes:
			phi *= (p[0]**(p[1]-1))*(p[0]-1)
		return phi
		
	@staticmethod
	def euclidGCD(a, b):
		a = Helpers.parsePositiveInt(a)
		b = Helpers.parsePositiveInt(b)
		if a < b:
			h = a
			a = b
			b = h
		while b > 0:
			h = a % b
			a = b
			b = h
		return a
		
	@staticmethod
	def primeFactorizedGCD(pas, pbs):
		for pa in pas:
			pa = Helpers.parsePositiveInt(pa[0])
			##TODO##
		return 0
		
	@staticmethod
	def halfFactorizedGCD(pas, b):
		b = Helpers.parsePositiveInt(b)
		##TODO##
		return 0
