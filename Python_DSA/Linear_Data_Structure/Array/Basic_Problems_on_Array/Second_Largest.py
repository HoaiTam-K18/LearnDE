# Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.

# Note: If the second largest element does not exist, return -1.

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.


# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.


# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 there is no second largest element.

def getSecondLargest(arr):
    largest = -1
    secondLargest = -1

    for i in arr:
        if i > largest:
            secondLargest = largest
            largest = i
        elif i > secondLargest and i < largest:
            secondLargest = i
    return secondLargest

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print(getSecondLargest(arr))

    # Time Complexity: O(n), as we are traversing the array only once.
    # Auxiliary space: O(1)
