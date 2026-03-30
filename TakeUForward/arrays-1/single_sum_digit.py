def single_sum(lst):
    total=0
    for num in lst:
        total = total+num

    while total>=10:
        sum=0
        while total>0:
            sum = sum+total%10
            total=total//10
        total = sum
    return total


_list= [1,2,3,4,5,6,7,8]
print(single_sum(_list))