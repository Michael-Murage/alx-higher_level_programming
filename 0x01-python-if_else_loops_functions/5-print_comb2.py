#!/usr/bin/python3
print('00', end='')
for i in range(1, 100):
    print(", {:0>2}".format(i), end='')
print("\n")
