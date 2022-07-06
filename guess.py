from collections import Counter
import random


def guess_word_1(valid_words):
    return random.choice(valid_words)


def guess_word_2(valid_words):
    count = Counter()
    for cur in valid_words:
        count.update(cur)
    top_words = []
    for cur in valid_words:
        unique_chars = set(cur)
        score = sum([count.get(c) for c in unique_chars])
        top_words.append((score, cur))
    return sorted(top_words, reverse=True)[0][1]
