# Given an array, arr of n integers, and an integer element x, find whether element x is present in the array. 
# Return the index of the first occurrence of x in the array, or -1 if it doesn’t exist.

# Input: arr[] = [1, 2, 3, 4], x = 3
# Output: 2
# Explanation: There is one test case with array as [1, 2, 3 4] and element to be searched as 3. Since 3 is present at index 2, the output is 2.


# Input: arr[] = [10, 8, 30, 4, 5], x = 5
# Output: 4
# Explanation: For array [1, 2, 3, 4, 5], the element to be searched is 5 and it is at index 4. So, the output is 4.


# Input: arr[] = [10, 8, 30], x = 6
# Output: -1
# Explanation: The element to be searched is 6 and its not present, so we return -1.

def search(arr, x):
    for i in arr:
        if i == x:
            return i
    return -1

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    x = 30
    
    # Function call
    result = search(arr, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)