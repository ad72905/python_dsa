# Reverse an input array using an algorithm that is in-place, i.e. without any extra memory
def reverse_array(input_array):
    print('Input Array : ', input_array)
    begin_index = 0
    end_index = len(input_array) - 1

    while end_index > begin_index:
        input_array[begin_index], input_array[end_index] = input_array[end_index], input_array[begin_index]
        begin_index = begin_index + 1
        end_index = end_index - 1

    print('Output Array : ', input_array)



