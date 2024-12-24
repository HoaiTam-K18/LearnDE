# Given an array of size n, the task is to check if it is sorted in ascending order or not. 
# Equal values are allowed in an array and two consecutive equal values are considered sorted.

# Input: arr[] = [20, 21, 45, 89, 89, 90]
# Output: Yes

# Input: arr[] = [20, 20, 45, 89, 89, 90]
# Output: Yes

# Input: arr[] = [20, 20, 78, 98, 99, 97]
# Output: No

def arraySortedOrNot1(arr):
    # Array has one or no element
    if len(arr) < 2:
        return True
    
    for i in range(len(arr) - 1):

        # Unsorted pair found
        if arr[i] > arr[i + 1]:
            return False
        
    # No unsorted pair found
    return True

def arraySortedOrNot2(arr, n):
    # Array has one or no element
    if n < 2:
        return True
    
    # Check if present index and index 
    # previous to it are in correct order
    # and rest of the array is also sorted
    # if true then return true else return
    # false
    return (arr[n - 1] >= arr[n - 2] and arraySortedOrNot2(arr, n - 1))


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    if arraySortedOrNot1(arr):
        print("YES")
    else:
        print("NO")

    # Recursive approach – O(n) Time and O(n) Space

    if arraySortedOrNot2(arr, len(arr)):
        print("YES")
    else:
        print("NO")

    # Time Complexity: O(n) 
    # uxiliary Space: O(n) for Recursion Call Stack.
