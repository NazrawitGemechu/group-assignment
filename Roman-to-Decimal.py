#Roman to Decimal Conversion

r=input("Enter roman numeral: ").upper()
def roman_to_decimal(r):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(r)):
        if i < len(r) - 1 and dict[r[i]] < dict[r[i+1]]:
            result -= dict[r[i]]
        else:
            result += dict[r[i]]
    return result


print(roman_to_decimal(r)) 