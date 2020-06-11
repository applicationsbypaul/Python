"""
Program: average_scores.py
Author: Paul Ford
Last date modified: 06/6/2020
Purpose: gather user information
display average score with information
"""


def average(score1, score2, score3):
    NUMBER_TESTS = 3
    if score1 < 0:
        raise ValueError
    return float((score1 + score2 + score3) / NUMBER_TESTS)


if __name__ == '__main__':
    pass
