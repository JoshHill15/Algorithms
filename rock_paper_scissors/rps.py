#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    options = ["rock", "paper", "scissors"]
    answer = []

    def arrayBuilder(arr, roundNumber):
        for i in range(len(options)):
            arr.append(options[i])
            if n == roundNumber:
                answer.append(arr[:])
            else:
                arrayBuilder(arr, roundNumber+1)
            arr.pop()
    arrayBuilder([], 1)
    return answer


print(rock_paper_scissors(2))
# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays = int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print('Usage: rps.py [num_plays]')
a = len([['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]
        )
b = len([['rock', 'rock', 'rock'], ['rock', 'rock', 'paper'], ['rock', 'rock', 'scissors'], ['rock', 'paper', 'rock'], ['rock', 'paper', 'paper'], ['rock', 'paper', 'scissors'], ['rock', 'scissors', 'rock'], ['rock', 'scissors', 'paper'], ['rock', 'scissors', 'scissors'], ['paper', 'rock', 'rock'], ['paper', 'rock', 'paper'], ['paper', 'rock', 'scissors'], ['paper', 'paper', 'rock'], ['paper', 'paper', 'paper'], ['paper',
                                                                                                                                                                                                                                                                                                                                                                                                                                 'paper', 'scissors'], ['paper', 'scissors', 'rock'], ['paper', 'scissors', 'paper'], ['paper', 'scissors', 'scissors'], ['scissors', 'rock', 'rock'], ['scissors', 'rock', 'paper'], ['scissors', 'rock', 'scissors'], ['scissors', 'paper', 'rock'], ['scissors', 'paper', 'paper'], ['scissors', 'paper', 'scissors'], ['scissors', 'scissors', 'rock'], ['scissors', 'scissors', 'paper'], ['scissors', 'scissors', 'scissors']])
c = len([['rock', 'rock', 'rock', 'rock'], ['rock', 'rock', 'rock', 'paper'], ['rock', 'rock', 'rock', 'scissors'], ['rock', 'rock', 'paper', 'rock'], ['rock', 'rock', 'paper', 'paper'], ['rock', 'rock', 'paper', 'scissors'], ['rock', 'rock', 'scissors', 'rock'], ['rock', 'rock', 'scissors', 'paper'], ['rock', 'rock', 'scissors', 'scissors'], ['rock', 'paper', 'rock', 'rock'], ['rock', 'paper', 'rock', 'paper'], ['rock', 'paper', 'rock', 'scissors'], ['rock', 'paper', 'paper', 'rock'], ['rock', 'paper', 'paper', 'paper'], ['rock', 'paper', 'paper', 'scissors'], ['rock', 'paper', 'scissors', 'rock'], ['rock', 'paper', 'scissors', 'paper'], ['rock', 'paper', 'scissors', 'scissors'], ['rock', 'scissors', 'rock', 'rock'], ['rock', 'scissors', 'rock', 'paper'], ['rock', 'scissors', 'rock', 'scissors'], ['rock', 'scissors', 'paper', 'rock'], ['rock', 'scissors', 'paper', 'paper'], ['rock', 'scissors', 'paper', 'scissors'], ['rock', 'scissors', 'scissors', 'rock'], ['rock', 'scissors', 'scissors', 'paper'], ['rock', 'scissors', 'scissors', 'scissors'], ['paper', 'rock', 'rock', 'rock'], ['paper', 'rock', 'rock', 'paper'], ['paper', 'rock', 'rock', 'scissors'], ['paper', 'rock', 'paper', 'rock'], ['paper', 'rock', 'paper', 'paper'], ['paper', 'rock', 'paper', 'scissors'], ['paper', 'rock', 'scissors', 'rock'], ['paper', 'rock', 'scissors', 'paper'], ['paper', 'rock', 'scissors', 'scissors'], ['paper', 'paper', 'rock', 'rock'], ['paper', 'paper', 'rock', 'paper'], ['paper', 'paper', 'rock', 'scissors'], ['paper', 'paper', 'paper', 'rock'], ['paper', 'paper', 'paper', 'paper'], ['paper', 'paper', 'paper', 'scissors'], ['paper', 'paper',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'scissors', 'rock'], ['paper', 'paper', 'scissors', 'paper'], ['paper', 'paper', 'scissors', 'scissors'], ['paper', 'scissors', 'rock', 'rock'], ['paper', 'scissors', 'rock', 'paper'], ['paper', 'scissors', 'rock', 'scissors'], ['paper', 'scissors', 'paper', 'rock'], ['paper', 'scissors', 'paper', 'paper'], ['paper', 'scissors', 'paper', 'scissors'], ['paper', 'scissors', 'scissors', 'rock'], ['paper', 'scissors', 'scissors', 'paper'], ['paper', 'scissors', 'scissors', 'scissors'], ['scissors', 'rock', 'rock', 'rock'], ['scissors', 'rock', 'rock', 'paper'], ['scissors', 'rock', 'rock', 'scissors'], ['scissors', 'rock', 'paper', 'rock'], ['scissors', 'rock', 'paper', 'paper'], ['scissors', 'rock', 'paper', 'scissors'], ['scissors', 'rock', 'scissors', 'rock'], ['scissors', 'rock', 'scissors', 'paper'], ['scissors', 'rock', 'scissors', 'scissors'], ['scissors', 'paper', 'rock', 'rock'], ['scissors', 'paper', 'rock', 'paper'], ['scissors', 'paper', 'rock', 'scissors'], ['scissors', 'paper', 'paper', 'rock'], ['scissors', 'paper', 'paper', 'paper'], ['scissors', 'paper', 'paper', 'scissors'], ['scissors', 'paper', 'scissors', 'rock'], ['scissors', 'paper', 'scissors', 'paper'], ['scissors', 'paper', 'scissors', 'scissors'], ['scissors', 'scissors', 'rock', 'rock'], ['scissors', 'scissors', 'rock', 'paper'], ['scissors', 'scissors', 'rock', 'scissors'], ['scissors', 'scissors', 'paper', 'rock'], ['scissors', 'scissors', 'paper', 'paper'], ['scissors', 'scissors', 'paper', 'scissors'], ['scissors', 'scissors', 'scissors', 'rock'], ['scissors', 'scissors', 'scissors', 'paper'], ['scissors', 'scissors', 'scissors', 'scissors']])

# print(a, b, c)
