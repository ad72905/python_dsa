def static_array():
    arr = [12, 23, 43, 56, 76]
    # print the array as is
    print(arr)
    # print size of the array
    print(len(arr))
    # print all elements of an array
    print(arr[:])
    # reverse the array with 0 gap
    print(arr[::-1])
    # reverse the array with 1 gap
    print(arr[::-2])
    # reverse the array with 2 gap
    print(arr[::-3])
    # reverse the array with 4 or more gap, result stays the same
    print(arr[::-5])
    # reverse the array with 5 gap
    print(arr[::-6])
    # reverse the array with 6 gap
    print(arr[::-7])
    # fetching sub-array up to index 3
    print(arr[1:4])
    # fetching sub-array up to index 4
    print(arr[1:5])
    # fetching sub-array up to beyond max index returns result up to max index in the array
    print(arr[1:7])
    # fetching first n items [0:n]
    print(arr[0:4])
    # fetching last n items [-n:]
    print(arr[-4:])
    # fetching all items except the last n items [:-n]
    print(arr[:-4])


if __name__ == '__main__':
    static_array()
