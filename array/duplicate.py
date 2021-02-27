# find duplicates in an array that has only positive elements and no element is greater in value than size of the array
def find_duplicates(int_array):
    print('Duplicates found :', end=' ')
    for i in int_array:
        if int_array[abs(i)] >= 0:
            int_array[abs(i)] = -int_array[abs(i)]
        else:
            print(abs(i), end=' ')
