#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ret_val = 0
    for k in range(x):
        try:
            print("{:d}".format(my_list[k]), end='')
            ret_val += 1
        except IndexError:
            break
    print("")
    return (ret_val)
