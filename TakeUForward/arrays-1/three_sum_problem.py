def three_sum_brute_force(nums, target):
    nums.sort()  # Optional: sort to keep triplets in order
    result = []

    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):  # j > i
            for k in range(j + 1, n):  # k > j
                if nums[i] + nums[j] + nums[k] == target:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in result:  # Avoid duplicates
                        result.append(triplet)

    return result


# Example usage
print(three_sum_brute_force([1, 2, 3, 4, 5, 6, 5, 3, 9], 8))
# Output: [[1, 2, 5], [1, 3, 4], [2, 3, 3]]