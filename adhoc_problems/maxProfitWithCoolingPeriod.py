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

    # no profit for an empty array or a single day price availability
    if price == [] or len(price) == 1:
        return 0

    # assuming local minimum to be at index zero
    buy = price[0]

    # building a profit capability array
    profit_cap = []

    # building profit array through the array
    for i in range(0, len(price)):
        buy = min(buy, price[i])
        profit_cap.append(price[i] - buy)

    # taking into account cooldown effect along profit capability on each day
    print(profit_cap)
    profit = 0
    for cool_down in range(2, len(profit_cap)):
        if profit_cap[cool_down] > 0:
            profit = max(profit, sum(profit_cap) - profit_cap[cool_down])

    return profit


# driver program
if __name__ == '__main__':
    print('Max Profit :', max_profit([1, 2, 3, 0, 2]))