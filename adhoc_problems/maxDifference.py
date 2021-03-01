# Buy Sell Stock Problem (buy-sell ONLY ONCE)

# We are given price of a stock on different days in an array
# We need to find out the maximum profit that can be earned by
# buying and selling that stock ONLY ONCE

# Condition : A new transaction can only start once the previous
# transaction is complete. That is essentially to say that you can
# hold only one stock at a time.

# Running time complexity : O(N)
# Space complexity : O(1)

def max_profit_method_one(price):

    j = 0
    profit = 0

    for i in range(1, len(price)):

        if price[i-1] > price[i]:
            j = i

        if price[i-1] <= price[i] and \
                (i + 1 == len(price) or price[i] >= price[i+1]):

            print('Local Minima :', price[j])
            print('Local Maxima :', price[i])
            profit = max(profit, price[i] - price[j])
            print('Profit :', profit)

    return profit

def max_profit_method_two(price):

    min_stock_value = price[0]
    max_profit = 0

    for p in price:
        max_profit = max(max_profit, p - min_stock_value)
        min_stock_value = min(p, min_stock_value)

    return max_profit


if __name__ == '__main__':
    print('Max Profit using 1st method :', max_profit_method_one([100, 180, 260, 310, 40, 535, 695]))
    print('Max Profit using 2nd method :', max_profit_method_two([100, 180, 260, 310, 40, 535, 695]))

