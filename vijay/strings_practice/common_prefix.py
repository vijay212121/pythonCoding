def longest_common_prefix(strs):
    if not strs:
        return ""

    # Start by assuming the whole first string is the prefix
    prefix = strs[0]

    for string in strs[1:]:
        # While the current string doesn't start with the prefix, shorten the prefix
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""


    return prefix


# Example usage
strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))  # Output: "fl"
