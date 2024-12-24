# Heap Sort Algorithm
# First convert the array into a max heap using heapify, Please note that this happens in-place. 
# The array elements are re-arranged to follow heap properties. Then one by one delete the root node of the Max-heap and replace it with the last node and heapify. 
# Repeat this process while size of heap is greater than 1.

# Rearrange array elements so that they form a Max Heap.
# Repeat the following steps until the heap contains only one element:
# Swap the root element of the heap (which is the largest element in current heap) with the last element of the heap.
# Remove the last element of the heap (which is now in the correct position). We mainly reduce heap size and do not remove element from the actual array.
# Heapify the remaining elements of the heap.
# Finally we get sorted array.

# Detailed Working of Heap Sort

# Step 1: Treat the Array as a Complete Binary Tree
# We first need to visualize the array as a complete binary tree. 
# For an array of size n, the root is at index 0, the left child of an element at index i is at 2i + 1, and the right child is at 2i + 2.

# Step 2: Build a Max Heap

# Step 3: Sort the array by placing largest element at end of unsorted array.

# To heapify a subtree rooted with node i
# which is an index in arr[].
def heapify(arr, n, i):
    
     # Initialize largest as root
    largest = i 
    
    #  left index = 2*i + 1
    l = 2 * i + 1 
    
    # right index = 2*i + 2
    r = 2 * i + 2  

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

# Main function to do heap sort
def heapSort(arr):
    
    n = len(arr) 

    # Build heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):
      
        # Move root to end
        arr[0], arr[i] = arr[i], arr[0] 

        # Call max heapify on the reduced heap
        heapify(arr, i, 0)

def printArray(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Driver's code
arr = [9, 4, 3, 8, 10, 2, 5] 
heapSort(arr)
print("Sorted array is ")
printArray(arr)