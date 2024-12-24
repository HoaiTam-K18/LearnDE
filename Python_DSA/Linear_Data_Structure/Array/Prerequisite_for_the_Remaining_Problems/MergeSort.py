# Merge sort is a sorting algorithm that follows the divide-and-conquer approach. 
# It works by recursively dividing the input array into smaller subarrays and sorting those subarrays then merging them back together to obtain the sorted array.

# In simple terms, we can say that the process of merge sort is to divide the array into two halves, sort each half, and then merge the sorted halves back together. 
# This process is repeated until the entire array is sorted.

# How does Merge Sort work?
# Merge sort is a popular sorting algorithm known for its efficiency and stability. It follows the divide-and-conquer approach to sort a given array of elements.

# Here’s a step-by-step explanation of how merge sort works:

# Divide: Divide the list or array recursively into two halves until it can no more be divided.
# Conquer: Each subarray is sorted individually using the merge sort algorithm.
# Merge: The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged.


# Divide: 

# [38, 27, 43, 10]  is divided into  [38, 27  ] and  [43, 10]  . 
# [38, 27]  is divided into  [38]  and  [27]  . 
# [43, 10]  is divided into  [43]  and  [10]  . 

# Conquer: 

# [38]  is already sorted. 
# [27]  is already sorted. 
# [43]  is already sorted. 
# [10]  is already sorted.
 
# Merge: 

# Merge  [38]  and  [27]  to get  [27, 38]  . 
# Merge  [43]  and  [10]  to get  [10,43]  . 
# Merge  [27, 38]  and  [10,43]  to get the final sorted list  [10, 27, 38, 43] 

# Therefore, the sorted list is  [10, 27, 38, 43]  .

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(len(L)):
        L[i] = arr[left + i]
    for j in range(len(R)):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j  < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j] 
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


# Driver code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    print(" ".join(map(str, arr)))

    merge_sort(arr, 0, len(arr) - 1)

    print("\nSorted array is")
    print(" ".join(map(str, arr)))