
num = input('Enter the Roman ')


def roman_to_decimal(r):
    dict_roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    number = 0
    for i in range(len(r)):
        if i+1 != len(r) and dict_roman[r[i]] < dict_roman[r[i+1]]:
            number = number - dict_roman[r[i]]
        else:
            number = number + dict_roman[r[i]]
    return number


print(roman_to_decimal(num))