# Buy Sell Stock Problem (buy-sell as many number of times as possible)

# We are given price of a stock on different days in an array
# We need to find out the maximum profit that can be earned by
# buying and selling that stock as many times as possible

# Condition : A new transaction can only start once the previous
# transaction is complete. That is essentially to say that you can
# hold only one stock at a time.

# Running time complexity : O(N)
# Space complexity : O(1)
def max_profit(price):

    # assuming local minimum to be at index zero
    j = 0
    # initializing profit to be zero
    profit = 0

    # iterating through stock prices for finding local min and local max
    # and adding up corresponding profits to arrive at max profit
    for i in range(1, len(price)):

        # if there is a decreasing trend in iteration, update the local min
        if price[i-1] > price[i]:
            j = i

        # check for the end of increasing sequence and then calc profit
        if price[i-1] <= price[i] and \
                (i+1 == len(price) or price[i] >= price[i+1]):
            print('Local Minima :', price[j])
            print('Local Maxima :', price[i])
            profit = profit + price[i] - price[j]

    # return max profit thus calculated
    return profit


if __name__ == '__main__':

    print('Profit :', max_profit([100, 180, 260, 310, 40, 535, 695]))