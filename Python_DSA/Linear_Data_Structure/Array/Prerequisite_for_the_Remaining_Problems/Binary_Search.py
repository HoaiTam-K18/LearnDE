# Binary Search Algorithm is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. 
# The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 

def binarySearch(arr, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def binarySearchRec(arr, left, right, x):
    if left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarySearchRec(arr, mid + 1, right, x)
        else:
            return binarySearchRec(arr, left, mid - 1, x)
    else:
        return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 10
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

    # Time Complexity: O(log N)
    # Auxiliary Space: O(1)

    # Recursive Binary Search Algorithm:
    arr = [2, 3, 4, 10, 40]
    x = 10
    
    # Function call
    result = binarySearchRec(arr, 0, len(arr)-1, x)
    
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
        
    # Time Complexity: 
    # Best Case: O(1)
    # Average Case: O(log N)
    # Worst Case: O(log N)
    # Auxiliary Space: O(1), If the recursive call stack is considered then the auxiliary space will be O(logN).