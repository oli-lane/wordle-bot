import guess
from evaluate import evaluate_word
from update import update_words


def main():
  print("Wordle Bot\n")
  word = input("Enter a word: ")
  solve(word)


def solve(word):
  num_guesses = 0
  with open('all_words.txt') as ifp:
    valid_words = list(map(lambda x: x.strip(), ifp.readlines()))
  while True:
    cur_guess = guess.guess_word_2(valid_words)
    num_guesses += 1
    print("Guess: " + cur_guess.upper())
    result = evaluate_word()  # 5 element array of nums 0, 1, or 2
    if num_guesses > 6:
      print("fail")
    # if result is correct
    if result == [2, 2, 2, 2, 2]:
      print("Your word took " + str(num_guesses) + " to solve!\n")
      break
    valid_words = update_words(valid_words, guess, result)


if __name__ == "__main__":
  main()
