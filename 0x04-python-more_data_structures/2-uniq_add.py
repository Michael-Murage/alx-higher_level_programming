#!/usr/bin/python3
def uniq_add(my_list=[]):
    arr = []
    count = 0
    for i in range(len(my_list)):
        if my_list[i] not in arr:
            arr.append(my_list[i])
            count += my_list[i]
    return count
