#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_result = []
    for i in range(len(my_list)):
        if (my_list[i] % 2 == 0):
            bool_result.append(True)
        else:
            bool_result.append(False)
    return bool_result
