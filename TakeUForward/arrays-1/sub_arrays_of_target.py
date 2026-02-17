def sub_arrays_with_target_sum(lst,target):
    result=list(set())
    for i in range(len(lst)):
        current_sum =0
        for j in range(i,len(lst)):
            current_sum=current_sum+lst[j]
            if current_sum == target:
                result.append(lst[i:j+1])
    return result


my_list = [1,2,3,4,-2,-4,3,2,-4,9,5]
tar=5
print(sub_arrays_with_target_sum(my_list,tar))