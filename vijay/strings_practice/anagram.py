'''
def is_anagram(str1, str2):
    # Sort both strings and check if they are equal
    return sorted(str1) == sorted(str2)


# Example usage
print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))  # Output: False
'''

'''
from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

# Example usage
print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))    # Output: False
'''

s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print("Not anagram")
else:
    count = {}

    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    for ch in s2:
        if ch not in count or count[ch] == 0:
            print("Not anagram")
            break
        count[ch] -= 1
    else:
        print("Anagram")