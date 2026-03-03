def max_sum_sub_lis(lst):
    # Initialize the sums with the first element
    current_sum = max_sum = lst[0]

    # Variables to track indices of the maximum sum subarray
    start = end = temp_start = 0

    # Loop through the list starting from the second element
    for i in range(1, len(lst)):
        # Decide: start a new subarray at lst[i] or extend the current subarray
        if lst[i] > current_sum + lst[i]:
            current_sum = lst[i]  # start new subarray
            temp_start = i        # temporary start index
        else:
            current_sum += lst[i]  # extend the current subarray

        # Update maximum sum and indices if current_sum exceeds max_sum
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start    # start index of max sum subarray
            end = i               # end index of max sum subarray

    # Return maximum sum and the subarray itself
    return max_sum, lst[start:end+1]


# Example usage
print(max_sum_sub_lis([-2,1,-3,4,-1,2,1,-5,4]))
# Output: (6, [4, -1, 2, 1])