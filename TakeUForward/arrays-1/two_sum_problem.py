def two_sum(lst,target):
    lst=list(set(lst))
    result=list(set())
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j]  == target:
                result.append([lst[i],lst[j]])
    return result

print(two_sum([1,2,3,4,5,6,5,3,9],8))