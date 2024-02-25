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

    function binary_to_decimal(binary_num) {
        let binary_str;
        
        if (typeof binary_num === 'number') {
            binary_str = String(binary_num);
        } else if (typeof binary_num === 'string') {
            binary_str = binary_num;
        } else {
            throw new TypeError("Input must be an integer or a string representing a binary number");
        }
        
        let decimal_num = 0;
        let power = binary_str.length - 1;
        
        for (let digit of binary_str) {
            if (!['0', '1'].includes(digit)) {
                throw new TypeError("Binary number must contain only '0' and '1'");
            }
            decimal_num += parseInt(digit) * Math.pow(2, power);
            power -= 1;
        }
        
        return decimal_num;
    }

    function decimal_to_any_base(decimal_num, base) {
        if (base < 2 || base > 33) {
            throw new ValueError("Base must be between 2 and 33");
        }
        if (decimal_num === 0) {
            return '0';
        }
        let any_base_num = '';
        while (decimal_num > 0) {
            let remainder = decimal_num % base;
            if (remainder < 10) {
                any_base_num = String(remainder) + any_base_num;
            } else {
                any_base_num = String.fromCharCode(remainder + 55) + any_base_num;
            }
            decimal_num = Math.floor(decimal_num / base);
        }
        return any_base_num;
    }

    console.log(binary_to_decimal(101)); // Output: 5

console.log(decimal_to_binary(12))