import unittest
from main import *


class TestBot(unittest.TestCase):
  def test_01(self) -> None:
    num_words = 0
    total_guesses = 0
    with open('all_words.txt') as ifp:
      test_words = list(map(lambda x: x.strip(), ifp.readlines()))
    for word in test_words:
      num_words += 1
      guesses = solve(word, "no")
      total_guesses += guesses
    avg = total_guesses / num_words
    print("The average number of guesses was " + str(avg) + "!\n")
    self.assertLess(avg, 6)

  def test_02(self) -> None:
    num_words = 0
    total_guesses = 0
    word = "trace"
    num_words += 1
    guesses = solve(word, "no")
    total_guesses += guesses
    avg = total_guesses / num_words
    print("The average number of guesses was " + str(avg) + "!\n")
