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

def add_in_base(number1, number2, base):
    result = ''
    carry = 0

    number1 = str(number1)
    number2 = str(number2)
    # Wyrównaj długości obu liczb
    number1 = number1.rjust(max(len(number1), len(number2)), '0')
    number2 = number2.rjust(max(len(number1), len(number2)), '0')

    # Dodawanie od końca
    for i in range(len(number1) - 1, -1, -1):
        sum = digit_to_value(number1[i]) + digit_to_value(number2[i]) + carry
        carry = sum // base
        result = value_to_digit(sum % base) + result

    if carry > 0:
        result = value_to_digit(carry) + result
    return result   


print(add_in_base(11,12,10))




