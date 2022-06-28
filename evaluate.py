

def evaluate(guess, answer):
    """
    5 element array of elements: 0, 1, or 2
    0 if character is not in answer
    1 if character is in answer but wrong index
    2 if character is in answer and correct index
    :param guess: string: 5 characters long
    :param answer: string: 5 characters long
    :return: List: 5 element array of elements: 0, 1, or 2
    """
    score = [0, 0, 0, 0, 0]
    # avg O(n^2)
    for i in range(5):
        if guess[i] == answer[i]:
            score[i] = 2
        elif guess[i] in answer:
            score[i] = 1

    return score
