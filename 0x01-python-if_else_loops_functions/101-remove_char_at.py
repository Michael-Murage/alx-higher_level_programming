#!/usr/bin/env python3
"""
creates a copy of the string, removing the character
 at the position n (not the Python way, the “C array index”).
"""

def remove_char_at(str, n):
    if n >= len(str) or n < 0:
        return str
    else:
        before = str[0:n]
        after = str[n+1:]
        return before + after
