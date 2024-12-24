# QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and 
# partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

# How does QuickSort Algorithm work?
# QuickSort works on the principle of divide and conquer, breaking down the problem into smaller sub-problems.

# There are mainly three steps in the algorithm:

# Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).
# Partition the Array: Rearrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, 
# and all elements greater than the pivot will be on its right. The pivot is then in its correct position, and we obtain the index of the pivot.
# Recursively Call: Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).
# Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.

# Partition function
def partition(arr, left, right):

    # Choose the pivot
    pivot = arr[right]

    # Index of smaller element and indicates 
    # the right position of pivot found so far
    i = left - 1

    # Traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Move pivot after smaller elements and
    # return its position
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1

# The QuickSort function implementation
def quickSort(arr, left, right):
    if left < right:
        # pi is the partition return index of pivot
        pivot = partition(arr, left, right)

        # Recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, left, pivot - 1)
        quickSort(arr, pivot + 1, right)

# Main driver code
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]

    quickSort(arr, 0, len(arr) - 1)
    
    print(" ".join(map(str, arr)))