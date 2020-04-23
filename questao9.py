def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    
    return True

assert(is_palindrome("abba"))
assert(not is_palindrome("abab"))
assert(is_palindrome("tenet"))
assert(not is_palindrome("banana"))
assert(is_palindrome("straw warts"))
assert(is_palindrome("a"))
assert(is_palindrome(""))