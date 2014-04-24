#/usr/local/bin/python

""" the plan is to recursively look for words that begin with the letter
    we are searching, printing words as we find them

    Here is the board

    L I G O
    E P N I
    N A C K
    S M A R
"""

english_dictionary = {}

search_word = []

boggle_board = [[]]

boggle_board[0].append("L")
boggle_board[0].append("I")
boggle_board[0].append("G")
boggle_board[0].append("O")


print boggle_board

