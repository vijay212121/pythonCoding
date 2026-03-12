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

# Two strings to compare
s1 = "listen"
s2 = "silent"

# Step 1: If lengths are different, they cannot be anagrams
if len(s1) != len(s2):
    print("Not anagram")
else:
    # Step 2: Create a dictionary to count characters in s1
    count = {}

    for ch in s1:
        # Increment count for each character
        # If character not in dict, get() returns 0
        count[ch] = count.get(ch, 0) + 1

    # Step 3: Decrease count for each character in s2
    for ch in s2:
        # If character not in s1 or already used up
        if ch not in count or count[ch] == 0:
            print("Not anagram")
            break
        count[ch] -= 1  # Use up one occurrence

    # Step 4: If loop completed without break, strings are anagrams
    else:
        print("Anagram")