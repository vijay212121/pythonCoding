def find_sum(num):
    num = int(num)
    while num>=10:
        sum = 0
        while num>0:
            sum = sum +num%10
            num=num//10
        num=sum
    return str(num)


_string = "my name is vijay 2676121 age 2345674 complete"
split_string = _string.split(' ')
result = []
for nm in split_string:
    if nm.isdigit():
        result.append(find_sum(nm))
    else:
        result.append(nm[::-1])
final_str = ' '.join(result)
print(final_str)
