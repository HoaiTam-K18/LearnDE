# Given an array, generate all the possible subarrays of the given array using recursion.

# Input : [1, 2, 3]
# Output : [1], [1, 2], [2], [1, 2, 3], [2, 3], [3]

# Input : [1, 2]
# Output : [1], [1, 2], [2]


# Recursive function to print all possible subarrays 
# for given array
def printSubArrays(arr, start, end):
    if end != len(arr):
        if start == end:
            # Increment the end point and start from 0
            print(arr[start:end + 1])
            return printSubArrays(arr, 0, end + 1)
        else:
            # Print the subarray and increment the starting
            print(arr[start:end + 1])
            return printSubArrays(arr, start + 1, end)


if __name__ == "__main__":
    arr =  [10, 20, 30, 40, 50]
    printSubArrays(arr, 0, 0)