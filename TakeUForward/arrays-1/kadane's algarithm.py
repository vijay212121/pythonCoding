"""
it's the same of max_sum_of_sub_array
"""


def kadane(arr):
    # Initialize max_sum and current_sum with the first element
    max_sum = arr[0]  # Best sum found so far
    current_sum = arr[0]  # Current subarray sum being considered

    # Loop through the array starting from the second element
    for i in range(1, len(arr)):
        # Either extend the current subarray or start new from arr[i]
        current_sum = max(arr[i], current_sum + arr[i])

        # Update max_sum if current_sum is bigger
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example usage
arr = [-2, 3, 2, -1, 4, -5, 2]
print(kadane(arr))  # Output: 8