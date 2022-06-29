import guess
from evaluate import evaluate_word


def main():
  solve()


def solve():
  num_guesses = 0
  with open('all_words.txt') as ifp:
    valid_words = list(map(lambda x: x.strip(), ifp.readlines()))
  while True:
    cur_guess = guess.guess_word_2(valid_words)
    num_guesses += 1
    print("Guess: " + cur_guess.upper())
    result = evaluate_word()
    if num_guesses > 6:
      print("fail")
      break
    if result == CORRECT:
      print("success")
      break
    valid_words = update_valid_words(valid_words, guess, result)


if __name__ == "__main__":
  main()
