def long_sub_string(s):
    left = 0                      # Left pointer of sliding window
    char_set = set()              # Stores unique characters in current window
    start_index = 0               # Starting index of longest substring found
    max_length = 0                # Length of longest substring found

    # Right pointer expands the window
    for right in range(len(s)):

        # If current character is already in the set,
        # shrink the window from the left
        while s[right] in char_set:
            char_set.remove(s[left])   # Remove left character from set
            left += 1                  # Move left pointer forward

        # Add current character to the set
        char_set.add(s[right])

        # Calculate current window length
        current_length = right - left + 1

        # Update maximum length and starting index if needed
        if current_length > max_length:
            max_length = current_length
            start_index = left

    # Return longest substring and its length
    return s[start_index:start_index + max_length], max_length


# Example
name = "cdasfghdd"
print(long_sub_string(name))

#Expand → Check duplicate → Shrink → Update max