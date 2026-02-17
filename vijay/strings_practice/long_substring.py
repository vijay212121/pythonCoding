def long_sub_string(s):
    left = 0
    char_set = set()
    start_index = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])

        current_length = right-left+1
        if current_length > max_length:
            max_length = current_length
            start_index = left
    return s[start_index:start_index+max_length], max_length

name = "cdasfghdd"
print(long_sub_string(name))

