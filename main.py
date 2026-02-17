def find_subarrays_with_target_sum(arr, target):
    from collections import defaultdict

    prefix_sum = 0
    prefix_map = defaultdict(list)  # maps prefix sum to list of indices
    prefix_map[0].append(-1)  # to handle subarrays starting from index 0

    result = []

    for i, num in enumerate(arr):
        prefix_sum += num

        # If (prefix_sum - target) exists, it means we found subarrays
        if (prefix_sum - target) in prefix_map:
            for start_index in prefix_map[prefix_sum - target]:
                result.append(arr[start_index + 1: i + 1])

        # Store the current prefix_sum with current index
        prefix_map[prefix_sum].append(i)

    return result

arr = [1, 8, 3, -2, -5]
target = 3
print(find_subarrays_with_target_sum(arr, target))