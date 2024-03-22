mapa_IC = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
    16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N',
    24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T',
    30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'
}

map_CI = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    **{chr(65 + i): i + 10 for i in range(26)}  # Maps 'A' to 10, 'B' to 11, ..., 'Z' to 35
}

def any_base_to_decimal(any_base_number, base):
    decimal_num = 0
    power = len(any_base_number) - 1
    for digit in any_base_number:
        decimal_num = map_CI[[digit] * (base ** power)]
        power -= 1
    return decimal_num

any_base_number = input("input number in choosen numerical system: ")
desired_base = input("input your desired base")
print(any_base_to_decimal(any_base_number, desired_base))

