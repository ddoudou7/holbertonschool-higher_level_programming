#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_val = my_list[0]
    for number in my_list:
        if number > max_val:
            max_val = number
    return max_val
