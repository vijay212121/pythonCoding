#here, three_sum for only k elements i.e.,3

def three_sum(lst,target):
    lst=list(set(lst))
    result=list(set())
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            for k in range(j,len(lst)):
                if lst[i] + lst[j] + lst[k] == target:
                    result.append([lst[i],lst[j],lst[k]])
    return result

print(three_sum([1,2,3,4,5,6,5,3,9],8))