def is_palindrome(s):
    return s == s[::-1]

# Test cases
print(is_palindrome("aca"))      # True
print(is_palindrome("aabbaa"))   # True
print(is_palindrome("abbbb"))    # False
print(is_palindrome("baabbb"))   # False
