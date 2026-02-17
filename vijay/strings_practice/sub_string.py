def find_substring(s, substring):
    # Use the find() method to locate the first occurrence of the substring
    return s.find(substring)

# Example usage
string = "hello world"
substring = "world"
print(find_substring(string, substring))  # Output: 6

substring = "python"
print(find_substring(string, substring))  # Output: -1
