#!/usr/local/bin/python

# Programming assignment from Lau Shr Mike

"""
Your job is to write a class that can support the following functionality:

m = Model()
m.buildModel(["apple", "ape", "ample"])
m.printPseudoRandom()
> ampppe
m.printStats()
> a starts a word 100% of the time.
> a is followed by p 66% of the time.
> a is followed by m 33% of the time.
> p is followed by p 25% of the time.
> p is followed by l 50% of the time.
> p is followed by e 25% of the time.
> l is followed by e 100% of the time.
> e ends a word 100% of the time.

You are building a statistical model called a Markov Chain (if you're curious) - but the point is I can feed an arbitrary list of random words to buildModel and produce a different model, all based on the input.  

You must implement the methods buildModel and printStats.  If you have time, do printPseudoRandom as well.  Since you'll be doing this on a computer you should be able to feed in simple input and test out your code, I did this in about 30 minutes but it'll take you longer since your'e rusty and probably don't know python as well.  Just take as long as you need, look up whatever syntax you want.
"""

class Student:
	def __init__(self, name):
		self.name = name
		self.attend = 0
		self.grades = []

