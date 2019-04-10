#!python

# def contains(text: str, pattern: str):
#     """Return a boolean indicating whether pattern occurs in text."""
#     assert isinstance(text, str), 'text is not a string: {}'.format(text)
#     assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
#     '''
#     First attempt compares slices of the string
#     slicing costs a lot of time so I refactored 
#     the code to optimize performance
#     '''
#     # pat_len = len(pattern)
#     # for i in range(len(text) - len(pattern) + 1):
#     #     print(pattern, text[i : i + pat_len] )
#     #     if pattern == text[i : i + pat_len]:
#     #         return True
#     # return False
#     pat_len = len(pattern)
#     for i in range(len(text) - pat_len + 1):
#         found = True
#         for j in range(pat_len):
#             if pattern[j] != text[i + j]:
#                 found = False
#         if found:
#             return True
#     return False

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    if pattern == '':
        return True
    index = 0
    for char in text:
        if char == pattern[index]:
            index += 1
            if index == len(pattern):
                return True
        else:
            index = 0
            if char == pattern[index]:
                index += 1
    return False


def find_index(text: str, pattern: str):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if pattern == '':
        return 0
    index = 0
    for i, char in enumerate(text):
        if char == pattern[index]:
            index += 1
            if index == len(pattern):
                return i - len(pattern) + 1
        else:
            index = 0
            if char == pattern[index]:
                index += 1
    return None

def find_all_indexes(text: str, pattern: str):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    pat_len = len(pattern)
    list_of_indexes = []
    if pat_len == 0:     # edge case
        for i in range(len(text)):
            list_of_indexes.append(i)
        return list_of_indexes
    for i in range(len(text) - pat_len + 1):
        found = True
        for j in range(pat_len):
            if pattern[j] != text[i + j]:
                found = False
        if found:
            list_of_indexes.append(i)
    return list_of_indexes

def test_string_algorithms(text: str, pattern: str):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
