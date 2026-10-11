# Problem:
# Write a function to reverse a given string.
def reverse_string(s: str) -> str:
    if (s == ""):
        return "Empty String"
    
    return s[::-1]

print(reverse_string("Hello"))


