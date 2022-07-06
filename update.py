from evaluate import *

def update_words(valid_words, cur_guess: str, result):
    """
    removes words that can't be guessed based on result
    simple O(n+m^2) solution
    :param valid_words: List of valid words
    :param cur_guess: 5 char word
    :param result: 5 element list indicating correctness of guess
    :return: List of updated valid words
    """
    return [word for word in valid_words if evaluate_word(cur_guess, word) == result]

