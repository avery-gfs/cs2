def binToDec(s):
    result = 0

    for d in s:
        result = result * 2 + int(d)

    return result

print(binToDec("11010")) # Should print 26

def decToBin(n):
    if n == 0:
        return "0"

    result = ""

    while n > 0:
        result = str(n % 2) + result
        n //= 2

    return result

print(decToBin(26)) # Should print 11010

hexValues = {
    "0":  0,
    "1":  1,
    "2":  2,
    "3":  3,
    "4":  4,
    "5":  5,
    "6":  6,
    "7":  7,
    "8":  8,
    "9":  9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
}

hexDigits = "0123456789abcdef"

def hexToDec(s):
    result = 0

    for d in s:
        result = result * 16 + hexValues[d]

    return result

print(hexToDec("1a")) # Should print 26

def decToHex(n):
    if n == 0:
        return "0"

    result = ""

    while n > 0:
        result = hexDigits[n % 16] + result
        n //= 16

    return result

print(decToHex(26)) # Should print 1a
