def digit_to_value(digit):
    if '0' <= digit <= '9':
        return ord(digit) - ord('0')
    else:
        return ord(digit.upper()) - ord('A') + 10

def value_to_digit(value):
    if value < 10:
        return chr(value + ord('0'))
    else:
        return chr(value - 10 + ord('A'))