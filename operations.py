def digit_to_value(digit):
    if '0' <= digit <= '9':
        return ord(digit) - ord('0')
    else:
        return ord(digit.upper()) - ord('A') + 10