def subset_sum(arr, target):
    result = []  # to store all valid subsets

    def backtrack(start, path, current_sum):
        # ✅ Base case: if current sum equals target, save the current path
        if current_sum == target:
            result.append(list(path))  # make a copy and store
            return

        # ⛔ Early stopping: if current sum exceeds target, no point in continuing
        if current_sum > target:
            return

        # 🔁 Loop through remaining elements starting from 'start'
        for i in range(start, len(arr)):
            # ➕ Include arr[i] in current subset
            path.append(arr[i])

            # 🔁 Recurse with next index and updated sum
            backtrack(i + 1, path, current_sum + arr[i])

            # 🔙 Backtrack: remove last element to try other possibilities
            path.pop()

    # 🔁 Start recursion from index 0, with empty path and sum 0
    backtrack(0, [], 0)

    return result

arr = [2, 3, 5]
target = 8
print(subset_sum(arr, target))
