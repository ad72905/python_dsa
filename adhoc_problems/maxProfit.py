def max_profit(array):

    i = 0
    j = 0
    profit = 0

    while j < len(array):

        j = i + 1
        while array[i] < array[i+1] and i + 1 < len(array):
            i = i + 1

        profit = profit + array[i] - array[j]

    return profit


if __name__ == '__main__':

    print(max_profit([100, 180, 260, 310, 40, 535, 695]))