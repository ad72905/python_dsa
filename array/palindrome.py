# using shortcut
def is_palindrome(input_string):
    print('Input String :', input_string)
    print('Reversed String :', input_string[::-1])
    if input_string == input_string[::-1]:
        print('Input and reversed strings are same')
        print('Hence, a palindrome')
        return True
    print('Input and reversed strings are not same')
    print('Hence, not a palindrome')
    return False


# using string reversal
def check_palindrome(input_string):
    print('Input String :', input_string)
    print('Reversed String :', reverse(input_string))
    if input_string == reverse(input_string):
        print('Indeed, a palindrome')
        return True
    print('Reversed string is not the same as input string')
    print('Hence, not a palindrome')
    return True


# String reversal method
def reverse(input_string):
    s = list(input_string)
    begin = 0
    end = len(s) - 1
    while end > begin:
        s[begin], s[end] = s[end], s[begin]
        begin = begin + 1
        end = end - 1
    return ''.join(s)
