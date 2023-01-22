#!/usr/bin/python3
def safe_print_integer(value):
    boolean = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        boolean = False
    return boolean
