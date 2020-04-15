#!/usr/bin/python

import argparse

# O(n)


def find_max_profit(prices):
    # buy, sell, sellIndex = float("inf"), 0, float("inf")
    buy = float("inf")
    sell = 0
    sellIndex = float("inf")
    for i in range(len(prices)):
        if prices[i] < buy and i <= sellIndex:
            buy = prices[i]
        elif prices[i] > sell:
            sell = prices[i]
            sellIndex = i
        total = sell - buy
    return total


# print(find_max_profit([1050, 270, 1540, 3800, 2]))  # 3530
print(find_max_profit([100, 90, 80, 50, 20, 10]))  # -10

# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
