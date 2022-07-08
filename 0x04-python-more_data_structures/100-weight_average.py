#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    av = 0
    div = 0
    for tup in my_list:
        av += tup[0] * tup[1]
        div += tup[1]
        return float(av / div)
