#/usr/local/bin/python

""" the plan is to recursively look for words that begin with the letter
    we are searching, printing words as we find them

    Here is the board

    L I G O
    E P N I
    N A C K
    S M A R
"""

def is_prefix_valid(search_word):
  return search_word.lookup(search_word)
  

english_dictionary = {}

search_word = []

boggle_board = [[]]

boggle_board[0].append("L")
boggle_board[0].append("I")
boggle_board[0].append("G")
boggle_board[0].append("O")
boggle_board[1].append("E")
boggle_board[1].append("P")
boggle_board[1].append("N")
boggle_board[1].append("I")

while letter_x < length(boggle_board[0]):
  while letter_y < 2:
     # assumes the board is the same dimensions in x&y
     print boggle_board[letter_x][letter_y]

     search_word.append boggle_board[letter_x][letter_y]

     # find out if there is a word with this prefix
     if (is_prefix_valid(search_word)):
       
     

print boggle_board

