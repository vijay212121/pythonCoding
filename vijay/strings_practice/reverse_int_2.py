_string = "my name is vijay 2121 age 24 complete"
str_split = _string.split(' ')
reverse_string = reversed(str_split)
result = []
for nm in reverse_string:
    if nm.isdigit():
        num = int(nm)
        sum = 0
        while num > 0:
            sum = sum + num % 10
            num = num // 10
        result.append(str(sum))
    else:
        result.append(nm[::-1])

final_str = ' '.join(result)
print(final_str)
