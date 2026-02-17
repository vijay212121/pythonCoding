from collections import defaultdict


def group_anagrams(strs):
    anagram_map = defaultdict(list)

    for string in strs:
        # Sort each string and use it as the key
        sorted_str = ''.join(sorted(string))
        anagram_map[sorted_str].append(string)

    return list(anagram_map.values())


# Example usage
strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strings))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
