# Buy Sell Stock Problem (buy-sell as many as times as possible with a
# COOL DOWN PERIOD OF ONE DAY)

# We are given price of a stock on different days in an array
# We need to find out the maximum profit that can be earned by
# buying and selling that stock as many times as possible but
# with a COOL DOWN PERIOD OF ONE DAY

# After selling a stock you are NOT allowed to buy a stock for the next 1 day
# which is referred to as the cool-down.

# Condition : A new transaction can only start once the previous
# transaction is complete. That is essentially to say that you can
# hold only one stock at a time. You must buy before you sell.

def max_profit(price):

    j = 0

    profit = 0

    for i in range(1, len(price)):

        # updating local minimum
        if price[i-1] > price[i]:
            j = i

        # storing all possible profits in all increasing sequences
        if price[i-1] <= price[i] and \
                (i + 1 == len(price) or price[i] >= price[i+1]):
            profit = profit + price[i] - price[j]
            i, j = i+2, i+2

    return profit


# driver program
if __name__ == '__main__':
    print('Max_Profit :', max_profit([1, 2, 3, 0, 2]))