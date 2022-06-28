from collections import Counter


def guess_word(valid_words):
    count = Counter()
    for cur in valid_words:
        count.update(cur)
    top_words = []
    for cur in valid_words:
        unique_chars = set(cur)
        score = sum([count.get(c) for c in unique_chars])
        top_words.append((score, cur))
    return sorted(top_words, reverse=True)[0][1]