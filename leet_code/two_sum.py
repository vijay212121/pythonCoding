def two_sum(lst,tar):
    for i in range(0,len(lst)-1):
        if lst[i]+lst[i + 1]==tar:
            return [i,i+1]
    return None

nums = [2,7,11,15]
target = 18
print(two_sum(nums,target))