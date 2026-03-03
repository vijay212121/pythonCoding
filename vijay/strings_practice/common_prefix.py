def longest_common_prefix(strs):
    # Step 1: Handle empty list
    if not strs:
        return ""

    # Step 2: Assume the entire first string is the prefix initially
    prefix = strs[0]

    # Step 3: Compare the prefix with the rest of the strings
    for string in strs[1:]:
        # While the current string does not start with the prefix
        while not string.startswith(prefix):
            # Shorten the prefix by removing the last character
            prefix = prefix[:-1]

            # If prefix becomes empty, there is no common prefix
            if not prefix:
                return ""

    # Step 4: Return the longest common prefix
    return prefix


# Example usage
strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))  # Output: "fl"
