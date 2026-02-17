def rotate_list(lst,n):
    result = []
    result.extend(lst[n:] + lst[:n])
    return result

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate_list(nums,k))