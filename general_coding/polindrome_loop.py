def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True


print(is_palindrome("madam"))   # True
print(is_palindrome("hello"))   # False

"""
text = "hello"
reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

print(reversed_text)
"""