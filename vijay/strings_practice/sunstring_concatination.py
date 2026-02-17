def findSubstring(s, words):
    if not s or not words:
        return []

    word_length = len(words[0])
    total_length = word_length * len(words)
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    result = []

    for i in range(word_length):
        left = i
        right = i
        current_count = 0
        current_map = {}

        while right + word_length <= len(s):
            word = s[right:right + word_length]
            right += word_length

            if word in word_count:
                current_map[word] = current_map.get(word, 0) + 1
                current_count += 1

                while current_map[word] > word_count[word]:
                    left_word = s[left:left + word_length]
                    left += word_length
                    current_map[left_word] -= 1
                    current_count -= 1

                if current_count == len(words):
                    result.append(left)
            else:
                left = right
                current_map.clear()
                current_count = 0

    return result


# Example usage
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words))  # Output: [0, 9]
