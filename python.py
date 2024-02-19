def decimal_to_binary(decimal_num) {
    if decimal_num == 0:
        return '0'
    binary_num - ''
    while decimal_num > 0:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num = decimal_num // 2
    return binary_num
}