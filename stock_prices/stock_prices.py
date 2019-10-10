#!/usr/bin/python

import argparse


def find_max_profit(prices):
    cost_price = prices[0]
    max_profit = 0

    for i in range(len(prices) - 1):
        profit = prices[i + 1] - cost_price
        if profit > max_profit or (max_profit == 0 and profit < 0):
            max_profit = profit
        if prices[i + 1] < cost_price:
            cost_price = prices[i + 1]

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
