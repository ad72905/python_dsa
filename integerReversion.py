# use string conversion and reversal
from palindrome import reverse


def reverse_integer(input_int):
    str_int = str(input_int)
    print('Input integer :', input_int)
    print('Reversed integer :', int(reverse(str_int)))
    return int(reverse(str_int))


# using neat mathematical trick

def integer_reversion(input_int):
    print('Input integer :', input_int)
    reversed_int = 0
    remainder = 0
    while input_int > 0:
        remainder = input_int % 10
        # int(input_int / 10), below is case of implicit integer division
        input_int = input_int // 10
        reversed_int = reversed_int * 10 + remainder

    print('Reversed integer :', reversed_int)
    return reversed_int
