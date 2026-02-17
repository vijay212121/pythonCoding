a = "my name vijay 113 my age 25"
a_split = a.split(' ')
result = []

for ch in a_split:
    if ch.isdigit():
        result.append(ch)
    else:
        result.append(ch[::-1])

print(result)

