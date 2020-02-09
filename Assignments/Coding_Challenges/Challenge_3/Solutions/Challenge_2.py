# 2. Push sys.argv to the limit
#
# Construct a rudimentary Python script that takes a series of inputs as a command from a bat file, and does something to them. The rules:
#
# Minimum of three arguments to be used.
# You must do something interesting in 15 lines or less within the Python file.
# Print or file generated output should be produced.

import sys

score = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1,  "f": 4,
         "g": 2, "h": 4,"i": 1, "j": 8, "k": 5, "l": 1,
         "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
         "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
         "y": 4,"z": 10}

word_list = []

word_list.append(sys.argv[1])
word_list.append(sys.argv[2])
word_list.append(sys.argv[3])

for word in word_list:
    score_scrabble = sum(score[c] for c in word.lower())
    print word.lower() + ", scores: " + str(score_scrabble)
