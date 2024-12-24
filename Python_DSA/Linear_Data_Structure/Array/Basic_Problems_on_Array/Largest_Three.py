# Given an array arr[], the task is to find the top three largest distinct integers present in the array.

# Note: If there are less than three distinct elements in the array, then return the available distinct numbers in descending

# Input: arr[] = [10, 4, 3, 50, 23, 90]
# Output: [90, 50, 23]


# Input: arr[] = [10, 9, 9]
# Output: [10, 9]
# There are only two distinct elements


# Input: arr[] = [10, 10, 10]
# Output: [10]
# There is only one distinct element


# Input: arr[] = []
# Output: []

def print3largest(arr):
    res = []
    first = -1
    second = -1
    third = -1

    for i in arr:
        if i > first:
            third = second
            second = first
            first = i
        elif i < first and i > second:
            third = second
            second =  i
        elif i < second and i > third:
            third = i
    
    if first != -1:
        res.append(first)
    if second != -1:
        res.append(second)
    if third != -1:
        res.append(third)

    return res

if __name__ == "__main__":
    arr = [10, 30, 20, 50, 40]
    res = print3largest(arr)
    print("Three largest elements are", res)

    # Time Complexity: O(n)
    # Auxiliary Space: O(1)