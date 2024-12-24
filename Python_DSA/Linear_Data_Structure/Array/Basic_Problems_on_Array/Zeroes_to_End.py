# Given an array of integers arr[], the task is to move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: arr[] = [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.


# Input: arr[] = [10, 20, 30]
# Output: arr[] = [10, 20, 30]
# Explanation: No change in array as there are no 0s.

# Input: arr[] = [0, 0]
# Output: arr[] = [0, 0]
# Explanation: No change in array as there are all 0s.

def pushZerosToEnd(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1

if __name__ == "__main__":
    arr = [10, 0, 20, 0, 0, 30]
    pushZerosToEnd(arr)
    print(" ".join(map(str, arr)))