def bubble_sort(lst):
    for i in range(0,len(lst)):
        for j in range(0,len(lst)-i-1):
            if lst[j] >lst[j+1]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst



list1 = [9,5,3,55,0,1,2,6,5]
print(bubble_sort(list1))