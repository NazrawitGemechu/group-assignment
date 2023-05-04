'''
program to convert Roman numbers into Decimal
'''
s = input('Enter the Roman number to be converted ')


def roman_to_decimal(s):
    ''' a dictionary representing the roman numbers with the 
    corresponding integre values
    '''

    d = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    decimal = 0
    for i in range(len(s)):
        if i+1 != len(s) and d[s[i]] < d[s[i+1]]:
            decimal = decimal - d[s[i]]
        else:
            decimal = decimal + d[s[i]]
    return decimal


print(roman_to_decimal(s))
