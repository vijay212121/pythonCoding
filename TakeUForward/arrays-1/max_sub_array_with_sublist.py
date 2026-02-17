def max_sum_sub_lis(lst):
    current_sum =max_sum=lst[0]
    start=end=temp_start=0

    for i in range(1, len(lst)):
        if lst[i]> current_sum+lst[i]:
            current_sum=lst[i]
            temp_start=i
        else:
            current_sum = current_sum+lst[i]

        if current_sum>max_sum:
            max_sum=current_sum
            start=temp_start
            end=i
    return max_sum,lst[start:end+1]

print(max_sum_sub_lis([-2,1,-3,4,-1,2,1,-5,4]))