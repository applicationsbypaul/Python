"""
Program: average_scores.py
Author: Paul Ford
Last date modified: 06/10/2020
Purpose: gather user information
display average score with information
"""


def average(score1, score2, score3):
    NUMBER_TESTS = 3
    if score1 < 0:
        raise ValueError
    elif score2 < 0:
        raise ValueError
    elif score3 < 0:
        raise ValueError
    return float((score1 + score2 + score3) / NUMBER_TESTS)


if __name__ == '__main__':
    try:
        print(average(10, 20, 30))
    except:
        print('Please enter all positive integers.')
