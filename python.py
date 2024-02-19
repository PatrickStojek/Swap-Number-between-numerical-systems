def decimal_to_binary(decimal_num) {
    if decimal_num == 0:
        return '0'
    binary_num - ''
    while decimal_num > 0:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num = decimal_num // 2
    return binary_num
}

def binary_to_decimal(binary_num):
    decimal_num = 0
    power = len(binary_num) - 1
    for digit in binary_num:
        decimal_num += int(digit) * (2** power)
        power -= 1
    return decimal_num

