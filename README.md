# wordle-bot
Approach: Each remaining word gets ranked by how many times each unique letter in that word appears in all of the remaining words. The guess uses the most common remaining letters to allow the bot to eliminate the maximum amount of words each guess.

Usage: User is prompted to input words to user interface one at a time, each guess the bot makes gets printed.

Testing: Test cases for 1 word, ~1000 words, and all words. Can be modified to test any input file of 5-letter words

Results: 4.6983 avg for all 12972 words

Oli Lane and Nick Bircher
