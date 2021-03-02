# Buy Sell Stock Problem (buy-sell ONLY ONCE)

# We are given price of a stock on different days in an array
# We need to find out the maximum profit that can be earned by
# buying and selling that stock ONLY ONCE

# Condition : A new transaction can only start once the previous
# transaction is complete. That is essentially to say that you can
# hold only one stock at a time. You must buy before you sell.

# Running time complexity : O(N)
# Space complexity : O(1)
def max_profit_method_one(price):
    # initializing the local minimum to be at index zero
    j = 0
    # initializing profit to be zero (useful for empty array, one-element array)
    profit = 0

    # iterating through stock prices, finding profits in each increasing sequence
    # comparing through each such successive profit until we hit the end of array
    for i in range(1, len(price)):

        # updating local minimum in case there is a decreasing sequence
        if price[i - 1] > price[i]:
            j = i

        # checking for potential profit
        if price[i - 1] <= price[i] and \
                (i + 1 == len(price) or price[i] >= price[i + 1]):
            print('Local Minima :', price[j])
            print('Local Maxima :', price[i])
            print('Profit :', price[i] - price[j])
            profit = max(profit, price[i] - price[j])

    # return the max profit achieved
    return profit


# Alternate approach
# Running time complexity : O(N)
# Space complexity : O(1)
def max_profit_method_two(price):
    # return zero for an empty list of stock prices
    if len(price) == 0:
        return 0

    # assuming the first element of array is the minimum
    # initializing the max profit to be zero
    min_stock_value, max_profit = price[0], 0

    # iterating through stock prices and updating max profit and min stock value
    for p in price:
        max_profit = max(max_profit, p - min_stock_value)
        min_stock_value = min(p, min_stock_value)

    # return max profit thus achieved after completion of iteration
    return max_profit


# driver program
if __name__ == '__main__':
    print('Max Profit using 1st method :', max_profit_method_one([100, 180, 260, 310, 40, 535, 695]))
    print('Max Profit using 2nd method :', max_profit_method_two([100, 180, 260, 310, 40, 535, 695]))
    print('Max Profit using 1st method :', max_profit_method_one([2, 11, 1, 4, 7]))
    print('Max Profit using 2nd method :', max_profit_method_two([2, 11, 1, 4, 7]))
