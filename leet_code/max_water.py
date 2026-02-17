

def max_area(lst):
    left = 0    #left pointer index
    right=len(lst)-1    #right pointer index
    max_area = 0
    while left<right:   #looping till left index greater than right
        height = min(lst[left],lst[right])
        length = right-left
        area = length*height
        max_area = max(area,max_area)

        if left<right:
            left+=1
        else:
            right-=1
    return max_area
height_list = [1,8,6,2,5,4,8,3,7]
print(max_area(height_list))