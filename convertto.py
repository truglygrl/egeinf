def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

x1 =  15**153 + 15**25-1564
print(convert_to(x1, 15))
print(str(convert_to(x1, 15)).count('e'))
