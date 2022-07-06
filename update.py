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
    temp = valid_words
    for word in valid_words:
        for i in range(5):
            if result[i] == 0:
                if cur_guess[i] in word:
                    temp.remove(word)
                    break
            if result[i] == 2:
                if cur_guess[i] != word[i]:
                    temp.remove(word)
                    break
            if result[i] == 1:
                if cur_guess[i] == word[i]:
                    temp.remove(word)
                    break
                if cur_guess[i] not in word:
                    temp.remove(word)
                    break
    return temp

