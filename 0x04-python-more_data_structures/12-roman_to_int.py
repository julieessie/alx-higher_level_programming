#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(roman_string)):
        if i > 0 and d[roman_string[i]] > d[roman_string[i - 1]]:
            num += d[roman_string[i]] - 2 * \
                d[roman_string[i - 1]]
        else:
            num += d[roman_string[i]]
            return num
