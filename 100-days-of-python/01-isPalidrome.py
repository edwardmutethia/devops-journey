#!/usr/bin/python3
# Problem Statement:
# Check if a string is a palindrome (reads the same forward
# and backward).
# `True` if palindrome, else `False`

def is_palindrome(s: str) -> bool:
    return s[::-1] == s

print(is_palindrome("racecar"))
print(is_palindrome("Python"))
 

