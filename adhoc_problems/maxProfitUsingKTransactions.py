# Buy Sell Stock Problem (buy-sell only K times)

# We are given price of a stock on different days in an array
# We need to find out the maximum profit that can be earned by
# buying and selling that stock up to K times

# Condition : A new transaction can only start once the previous
# transaction is complete. That is essentially to say that you can
# hold only one stock at a time. You must buy before you sell.

def max_profit(price, allowed_transactions):

    j = 0

    profits = []

    trans_frequency = 0

    prof = 0

    for i in range(1, len(price)):

        # updating local minimum
        if price[i-1] > price[i]:
            j = i

        # storing all possible profits in all increasing sequences
        if price[i-1] <= price[i] and \
                (i + 1 == len(price) or price[i] >= price[i+1]):

            profits.append(price[i] - price[j])

    print('Profit possibilities :', profits)

    while len(profits) > 0:
        prof = prof + max(profits)
        del profits[profits.index(max(profits))]
        trans_frequency = trans_frequency + 1
        if trans_frequency == allowed_transactions:
            return prof

    return prof


# driver program
if __name__ == '__main__':
    print('Max_Profit :', max_profit([100, 180, 260, 310, 40, 535, 695],1))
    print('Max_Profit :', max_profit([3, 3, 5, 0, 0, 3, 1, 4],1))
    print('Max_Profit :', max_profit([1, 2, 3, 4, 5], 1))
    print('Max_Profit :', max_profit([7, 6, 4, 3, 1], 1))