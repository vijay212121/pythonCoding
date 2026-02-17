from collections import Counter

input_string = "swiss"
occurrence = Counter(input_string)
print(type(occurrence))
print(occurrence)

# Iterate over the string in original order to find the first non-repeating character
for char in input_string:
    if occurrence[char] == 1:
        print(char)
        break  # Stop after finding the first non-repeating character
