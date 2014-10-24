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
  def __init__(self):
    self.wordList = ""
    # char_couplets is the dictionary where we'll be storing the 
    # pairs of characters and the number of times they appear.  
    # using this we'll be able to calculate the probability of one
    # char following another.
    self.char_couplets = {}

    # char_starts is the dict where we keep track of all of the 
    # letters which are followed by another letter
    self.char_starts = {}

    # word_starts is the dict where we keep track of all of the 
    # letters which start words
    self.word_starts = {}

    # word_ends is the dict where we keep track of all of the 
    # letters which end words
    self.word_ends = {}

  def printList(self, wordList):
    print "DEBUG:  wordList is " + str(wordList)

  def buildModel(self, wordList):

    # pick up the wordList from the invocation
    self.wordList = wordList

    # let's iterate through the words and 
    # collect the characters in doubles
  
    # let's also collect all of the starts 
    # of the couplets to keep track of the 
    # denominator for our probabilities later.
    # It's nicer to do it in the same loop.

    for word in model1.wordList:
      # print "DEBUG: word is " + word
      # i = counter for iterating through the word
      i = 0
      word_start = word[:1]
      word_end = word[-1:]
      if word_start in model1.word_starts:
        # print "DEBUG: start found" + str(model1.word_starts)
        model1.word_starts[word_start] += 1.0
      else:
        model1.word_starts[word_start] = 1.0
        # print "DEBUG: start not found" + str(model1.word_starts)
        
      if word_end in model1.word_ends:
        model1.word_ends[word_end] += 1.0
      else:
        model1.word_ends[word_end] = 1.0

      while i < (len(word)-1):
        char_start = word[i:i+1]
        char_couple = word[i:i+2]
        # print "DEBUG: " + char_couple
  
        if char_start in model1.char_starts:
          model1.char_starts[char_start] += 1.0
        else:
          model1.char_starts[char_start] = 1.0
        if char_couple in model1.char_couplets:
          model1.char_couplets[char_couple] += 1.0
        else:
          model1.char_couplets[char_couple] = 1.0
        i += 1
    
    # MAINT:  this used to sort correctly, but now it doesn't.
    #         Apparently these get turned into lists after being
    #         sorted and lose their dictionaryness.  :(
    # model1.char_couplets = sorted(model1.char_couplets)
    # model1.char_starts = sorted(model1.char_starts)
    # model1.word_starts = sorted(model1.word_starts)
    return ()

  def printStats(self, char_couplets, char_starts, word_starts):
    # Cool, now we can work out the probabilities by looking at 
    # the second letters.  
  
    # print "DEBUG: " + str(model1.word_starts)
    for start in model1.word_starts:
      # print "DEBUG: " + start
      # print "DEBUG: " + str(model1.word_starts[start])
      # print "DEBUG: " + str(len(model1.wordList))
      word_start_probability = model1.word_starts[start]/len(model1.wordList) 
      # print "DEBUG: word_start_probability = " + str(word_start_probability)
      print str(start) + " starts a word " + \
      str("{0:.0f}%".format(word_start_probability*100)) + \
      " of the time"

    for couplet in model1.char_couplets:
      couplet_term1 = couplet[:1]                                             
      couplet_term2 = couplet[1:2]
      # We can get the probabilities by dividing the number of 
      # couplets by the number of starts
      #
      couplet_probability = char_couplets[couplet] / char_starts[couplet_term1]
      print couplet_term1 + " is followed by " + couplet_term2 + \
      " " + str("{0:.0f}%".format(couplet_probability*100)) + \
      " of the time"

    for end in model1.word_ends:
      # print "DEBUG: model1.word_ends[end] " + str(model1.word_ends[end])
      word_end_probability = model1.word_ends[end]/len(model1.wordList) 
      print str(end) + " ends a word " + \
      str("{0:.0f}%".format(word_end_probability*100)) + \
      " of the time"
  
# just instantiate the model
model1 = Model()

# build the model here with wordlist
model1.buildModel(["apple", "ape", "ample","banana"])

# print the word list for debugging
model1.printList(model1.wordList)

# print out the stats
model1.printStats(model1.char_couplets, model1.char_starts, model1.word_starts)

