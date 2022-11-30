#!/usr/bin/python3
# print('00', end='')
for i in range(0, 100):
    if (i == 99):
        print("99")
    else:
        print("{:0>2}".format(i), end=', ')
