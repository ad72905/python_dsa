# O(Nlog(N)) + O(N) = O(Nlog(N))
def is_anagram(input_string, candidate_string):
    print('Input String :', input_string)
    print('Candidate String :', candidate_string)

    if len(input_string) != len(candidate_string):
        print('Length not equal, hence not anagrams')
        return False

    input_string = list(input_string)
    candidate_string = list(candidate_string)

    # O(Nlog(N))
    sorted_input = sorted(input_string)
    sorted_candidate = sorted(candidate_string)

    # O(N)
    for i in range(len(sorted_input)):
        if sorted_input[i] != sorted_candidate[i]:
            print('Characters at position', str(i + 1), 'don\'t match')
            print('Hence, not anagrams')
            return False
    print('Indeed, they are anagrams')
    return True
