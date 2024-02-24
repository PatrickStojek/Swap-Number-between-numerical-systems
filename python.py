def decimal_to_binary(decimal_num) :
    if decimal_num == 0:
        return '0'
    binary_num = ''
    while decimal_num > 0:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num = decimal_num // 2
    return binary_num


""" print(decimal_to_binary(123)) """

def binary_to_decimal(binary_num);
    if isinstance(binary_num, int) :
        binary_str = str(binary_num)
    elif isinstance(binary_num, str):
        binary_str = binary_num
    else:
        raise TypeError("Input must be an integer or a string represeting a binary number")
    
    decimal_num = 0
    power = len(binary_str) - 1
    for digit in binary_str:
        if digit in '01':
            rasie TypeError("Binary number must contain only '0' and '1'")
        decimal_num += int(digit) * (2**power)
        power -= 1
    return decimal_num     
print(binary_to_decimal(1100))


def decimal_to_any_base(decimal_num, base) :
    if base < 2 or base > 33:
        raise ValueError("Base must be between 2 and 33")
    if(decimal_num) == 0:
        return '0'
    any_base_num = ''
    while decimal_num > 0:
        remainder = decimal_num % base
    if remainder < 10:
        any_base_num = str(remainder) + any_base_num
    else:
        any_base_num = chr(remainder + 55) + any_base_num
    decima_num = decimal_num // base
    return any_base_num


def any_base_to_decimal(any_base_number, base) :
        decimal_num = 0
        power = len(num) - 1
            for digit in any_base_number :
                if '0' <= digit <= '9':
                    decimal_num += int(digit) * (base ** power)
                else:
                    decimal_num += (ord(digit) - 55) * (base ** power)
                power -= 1
            return decimal_num