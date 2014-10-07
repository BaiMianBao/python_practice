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

	def addGrade(self, grade):
		self.grades.append(grade)

class Model:
	def __init__(self, wordList):
		self.wordList = wordList
		
	def printList(self, wordList):
		print wordList

model1 = Model(["apple","ape","ample"])
print model1.wordList

# char_couplets is the dictionary where we'll be storing the 
# pairs of characters and the number of times they appear.  
# using this we'll be able to calculate the probability of one
# char following another.
char_couplets = {}

# char_starts is the dict where we keep track of all of the 
# letters which are followed by another letter
char_starts = {}

# let's iterate through the words and 
# collect the characters in doubles

# let's also collect all of the starts 
# of the couplets to keep track of the 
# denominator for our probabilities later.
# It's nicer to do it in the same loop.

for word in model1.wordList:
	print word
	# i = number of char couples
	i = 0
	# j = number of starting letters
	j = 0
	while i < (len(word)-1):
		char_start = word[i:i+1]
		char_couple = word[i:i+2]
		print char_couple
		if char_start in char_starts:
			char_starts[char_start] += 1
		else:
			char_starts[char_start] = 1
		j += 1
		if char_couple in char_couplets:
			char_couplets[char_couple] += 1
		else:
			char_couplets[char_couple] = 1
		i += 1
	
# Cool, now we can work out the probabilities by looking at 
# the second letters.  Let's sort the char_couplets

char_couplets_sorted = sorted(char_couplets)
char_starts_sorted = sorted(char_starts)
print char_couplets_sorted
print char_starts

# We can get the probabilities by dividing the number of 
# couplets by the number of starts

# return (char_couplets_sorted, char_starts_sorted)

