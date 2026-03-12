def bubble_sort(lst):
    # Repeat for each element
    for i in range(0,len(lst)):
        # Compare adjacent elements
        for j in range(0,len(lst) - i - 1):
            # Swap if elements are in wrong order
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


# Example usage
list1 = [9, 5, 3, 55, 0, 1, 2, 6, 5]
print(bubble_sort(list1))  # Output: [0, 1, 2, 3, 5, 5, 6, 9, 55]

'''
1️⃣ Why len(lst) - i - 1?
len(lst) → total elements in the list
- i → after each outer loop pass, the last i elements are already sorted, so we don’t need to compare them again
- 1 → because we are comparing lst[j] with lst[j+1], we stop one element earlier to avoid going out of bounds
'''

