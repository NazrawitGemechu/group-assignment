roman = input('Enter the Roman number  ')


def converter(num):

    dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    decimal_num = 0
    for i in range(len(num)):
        if i+1 != len(num) and dict[num[i]] < dict[num[i+1]]:
            decimal_num = decimal_num - dict[num[i]]
        else:
            decimal_num = decimal_num + dict[num[i]]
    return decimal_num


print(converter(roman))