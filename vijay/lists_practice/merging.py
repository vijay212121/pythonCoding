def merge_alternate(list1, list2):
    merged_list = []  # Step 1: Create an empty list to store the result
    length = min(len(list1), len(list2))  # Step 2: Find the shorter list's length

    # Step 3: Add elements alternately
    for i in range(length):
        merged_list.append(list1[i])  # Add from list1
        merged_list.append(list2[i])  # Add from list2

    # Step 4: Append remaining elements from the longer list
    merged_list.extend(list1[length:])  # Remaining elements from list1
    merged_list.extend(list2[length:])  # Remaining elements from list2

    return merged_list  # Return the final merged list

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8, 10, 12]
print(merge_alternate(list1, list2))
