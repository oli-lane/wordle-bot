import guess
from evaluate import evaluate_word
from update import update_words


def main():
  print("Wordle Bot\n")
  while True:
    response = input("Do you want to play (y/n): ")
    if response == 'n':
      break
    word = input("Enter a word: ")
    num = solve(word, "yes")
    print("The Wordle bot solved " + word + " in " + str(num) + " guesses!")
  print("Thanks for playing!")


def solve(word, verbosity) -> int:
  num_guesses = 1
  with open('all_words.txt') as ifp:
    valid_words = list(map(lambda x: x.strip(), ifp.readlines()))
  # first guess is always crane
  result = evaluate_word("crane", word)
  valid_words = update_words(valid_words, "crane", result)
  if verbosity == "yes":
      print("Guess 1 : CRANE")
  while True:
    if result == [2, 2, 2, 2, 2]:
      return num_guesses
    cur_guess = guess.guess_word_2(valid_words)
    num_guesses += 1
    if verbosity == "yes":
      print("Guess " + str(num_guesses) + " : " + cur_guess.upper())
    result = evaluate_word(cur_guess, word)  # 5 element array of nums 0, 1, or 2
    valid_words = update_words(valid_words, cur_guess, result)


if __name__ == "__main__":
  main()
