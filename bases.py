#!python

import string
from math import floor, log
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace
string_of_digits = string.digits + string.ascii_lowercase


def decode(digits: str, base: int) -> int:
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    digits = digits.lower()

    # quick optimization
    if base == 10:
        return int(digits)

    # this will increment through the loop
    # i will increment for each exponent
    output = 0
    for i, digit in enumerate(reversed(digits)):
        output += string_of_digits.index(digit) * (base ** i)
    # print(output)
    return output



def encode(number: int, base: int) -> str:
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    # this finds the exponent to start counting down with
    power = floor(log(number, base))
    # output will be added to this string
    output = ''
    # this loops through each exponent subtracting the value from the number and adding to the string
    while number != 0:
        exponential_number = base ** power
        new_digit_index = 0
        # while number >= exponential_number:
        #     number -= exponential_number
        #     new_digit_index += 1
        new_digit_index = floor(number / exponential_number)
        number = number % exponential_number
        new_digit = string_of_digits[new_digit_index]
        output += new_digit
        power -= 1
        if number == 0:
            for i in range(power + 1):
                output += "0"

    print(output)
    # output = "hello"
    return output

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    return encode(int(decode(digits, base1)), base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    elif len(args) == 2:
        encode(int(args[0]), int(args[1]))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
