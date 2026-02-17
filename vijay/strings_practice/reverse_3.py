name = "asdfg ddv 56 rfv"
split_name = name.split(' ')
split_name.reverse()
result = []
for nm in split_name:
    if nm.isdigit():
        result.append(nm)
    else:
        result.append(nm[::-1])
print(' '.join(result))

