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
        decimal_num += map_CI[digit] * (base ** power)
        power -= 1
    return decimal_num 

def decimal_to_any_base(decimal_num, base):
    any_base_num = ''
    while decimal_num > 0:
        r = decimal_num % base
        any_base_num = mapa_IC[r] + any_base_num
        decimal_num = decimal_num // base
    return any_base_num

def tab_residual(base, integer_number):
    tab_resid = []
    while integer_number > 0:
        r = integer_number % base
        tab_resid.append(r)
        integer_number = integer_number // base
    return tab_resid

def number_conv(tab_resid):
    numb_conv = ''
    s = len(tab_resid)
    for i in range(s - 1, -1, -1):
        numb_conv += mapa_IC[tab_resid[i]]
    return numb_conv

def execution():
    p = int(input("Podaj podstawe systemu od 2 do 36 = "))
    n = int(input("Podaj liczbe całkowitą > 0 = "))
    print(number_conv(tab_residual(p, n)))

def main():
    choice = input("Wybierz opcję (1 - aby zamienić liczbę na system dziesiętny, 2 - aby zamienić liczbę z systemu dziesiętnego): ")
    if choice == '1':
        any_base_number = input('Podaj liczbę w dowolnym systemie: ')
        desired_base = int(input('Podaj podstawę jaką chcesz osiągnąć: '))
        print(any_base_to_decimal(any_base_number, desired_base))
    elif choice == '2':
        decimal_num = int(input("Podaj liczbę dziesiętną: "))
        desired_base = int(input("Podaj podstawę jaką chcesz osiągnąć: "))
        print(decimal_to_any_base(decimal_num, desired_base))
    else:
        print("Niepoprawny wybór.")

if __name__ == "__main__":
    main()
