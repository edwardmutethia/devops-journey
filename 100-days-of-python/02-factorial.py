#!/usr/bin/python3
# **Problem Statement:**
# Compute the factorial of a given integer `n`.
# Constraints:
# 0 <= n <= 20

def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))  # Output: 120