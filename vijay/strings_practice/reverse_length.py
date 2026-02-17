input_name = "bathini vijaya kumar"
split_name = input_name.split()
combined_name = ''.join(split_name)
rev_string = combined_name[::-1]
names_length = [len(nm) for nm in split_name]
print(names_length)

result = []
index = 0
for length in names_length:
    result.append(rev_string[index:index+length])
    index = index+length
print(' '.join(result))

