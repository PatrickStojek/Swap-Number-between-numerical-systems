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


def decimal_to_other_base(decimal_num, base):
    if not isinstance(decimal_num, int) or not isinstance(base, int):
        return "Both inputs must be integers"
    if base < 2:
        return "Base must be greater than or equal to 2"
    
    result = ""
    while decimal_num > 0:
        remainder = decimal_num % base
        result = str(remainder) + result
        decimal_num //= base
    
    return result if result else "0"

# Example usage:
decimal_num = 42
base = 2
print(f"Decimal {decimal_num} in base {base}: {decimal_to_other_base(decimal_num, base)}")

base = 8
print(f"Decimal {decimal_num} in base {base}: {decimal_to_other_base(decimal_num, base)}")

base = 16
print(f"Decimal {decimal_num} in base {base}: {decimal_to_other_base(decimal_num, base)}")
