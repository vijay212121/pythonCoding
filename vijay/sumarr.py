def sum_num(arr, num):
    for i in range(0,len(arr)):
        if arr[i]+arr[i+1] == num:
            return i, i+1
    return None


a= [4,5,6,7,8]
_num = 13
print(sum_num(a, _num))
