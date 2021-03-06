#!python


import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    '''time complexity:
            min time: O(1) if not palindrome on first check
            max time: O(n) if it is a palindrome'''
    text = refine_text(text)
    left = 0
    right = len(text) -1
    while right >= left:
        if text[left] != text[right]:
            return False
        right -= 1
        left += 1
    return True


def is_palindrome_recursive(text, left=0, right=None):
    '''time complexity:
        min time: O(1) if not palindrome on first check
        max time: O(n) if it is a palindrome'''
    text = refine_text(text)
    if right == None:
        right = len(text) - 1
    if right < left:
        return True
    elif text[left] != text[right]:
        return False
    return is_palindrome_recursive(text, left + 1, right -1)

LETTERS = frozenset(string.ascii_letters) # this is a set of letters that is quick

def refine_text(text):
    '''time complexity:
        min time: O(n)
        max time: O(n)'''
    text = text.lower()
    exclusions = "?.-! ,'"
    for char in exclusions:
        text = text.replace(char, '')
    return text


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
