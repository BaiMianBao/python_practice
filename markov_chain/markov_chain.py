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

class Model:
  def __init__(self, wordList):
    self.wordList = wordList
    
  def printList(self, wordList):
    print wordList

  def buildModel(self, wordList):
    # char_couplets is the dictionary where we'll be storing the 
    # pairs of characters and the number of times they appear.  
    # using this we'll be able to calculate the probability of one
    # char following another.
    char_couplets = {}

    # char_starts is the dict where we keep track of all of the 
    # letters which are followed by another letter
    char_starts = {}

    # word_starts is the dict where we keep track of all of the 
    # letters which start words
    word_starts = {}

    # word_ends is the dict where we keep track of all of the 
    # letters which end words
    word_ends = {}

    # let's iterate through the words and 
    # collect the characters in doubles
  
    # let's also collect all of the starts 
    # of the couplets to keep track of the 
    # denominator for our probabilities later.
    # It's nicer to do it in the same loop.

    for word in model1.wordList:
      # DEBUG: print word
      # i = counter for iterating through the word
      i = 0
      word_start = word[:1]
      word_end = word[-1:]
      if word_start in word_starts:
        # print "DEBUG: start found" + str(word_starts)
        word_starts[word_start] += 1.0
      else:
        word_starts[word_start] = 1.0
        # print "DEBUG: start not found" + str(word_starts)
        
      if word_end in word_ends:
        word_ends[word_end] += 1.0
      else:
        word_ends[word_end] = 1.0

      while i < (len(word)-1):
        char_start = word[i:i+1]
        char_couple = word[i:i+2]
        # print "DEBUG: " + char_couple
  
        if char_start in char_starts:
          char_starts[char_start] += 1.0
        else:
          char_starts[char_start] = 1.0
        if char_couple in char_couplets:
          char_couplets[char_couple] += 1.0
        else:
          char_couplets[char_couple] = 1.0
        i += 1
    
    char_couplets_sorted = sorted(char_couplets)
    char_starts_sorted = sorted(char_starts)
    return (char_couplets_sorted, char_starts_sorted)

  def printStats(char_couplets_sorted, char_starts_sorted):
    # Cool, now we can work out the probabilities by looking at 
    # the second letters.  
  
    print "DEBUG: " + str(word_starts)
    for start in word_starts:
      # print "DEBUG: " + start
      # print "DEBUG: " + str(word_starts[start])
      # print "DEBUG: " + str(len(model1.wordList))
      word_start_probability = word_starts[start]/len(model1.wordList) 
      # print "DEBUG: word_start_probability = " + str(word_start_probability)
      print str(start) + " starts a word " + \
      str("{0:.0f}%".format(word_start_probability*100)) + \
      " of the time"

    for couplet in sorted(char_couplets):
      couplet_term1 = couplet[:1]                                             
      couplet_term2 = couplet[1:2]
      # We can get the probabilities by dividing the number of 
      # couplets by the number of starts
      #
      couplet_probability = char_couplets[couplet] / char_starts[couplet_term1]
      print couplet_term1 + " is followed by " + couplet_term2 + \
      " " + str("{0:.0f}%".format(couplet_probability*100)) + \
      " of the time"

    for end in word_ends:
      print "DEBUG: word_ends[end] " + str(word_ends[end])
      word_end_probability = word_ends[end]/len(model1.wordList) 
      print str(end) + " ends a word " + \
      str("{0:.0f}%".format(word_end_probability*100)) + \
      " of the time"
  
  model1 = Model(["apple","ape","ample","banana"])
  print "DEBUG:  model1.wordList: " + str(model1.wordList)
  buildModel(model1)
