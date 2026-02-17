def is_anagram(str1, str2):
    # Sort both strings and check if they are equal
    return sorted(str1) == sorted(str2)


# Example usage
print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))  # Output: False


# from collections import Counter
#
# def is_anagram(str1, str2):
#     return Counter(str1) == Counter(str2)
#
# # Example usage
# print(is_anagram("listen", "silent"))  # Output: True
# print(is_anagram("hello", "world"))    # Output: False
