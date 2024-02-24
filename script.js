function decimal_to_binary(decimal_num) {
    if(decimal_num == 0) {
        return '0'
    }
    const binary_num = ''
    while (decimal_num > 0)  {
        binary_num = String(decimal_num % 2) + binary_num
        decimal_num = Math.floor(decimal_num / 2)
    }
    return binary_num
}

console.log(decimal_to_binary(12))