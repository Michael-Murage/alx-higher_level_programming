#!/usr/bin/python3
x = ''
for letter in range(97, 123):
    if chr(letter):
        x += chr(letter)
print("{}".format(x[::-1]), end="")
