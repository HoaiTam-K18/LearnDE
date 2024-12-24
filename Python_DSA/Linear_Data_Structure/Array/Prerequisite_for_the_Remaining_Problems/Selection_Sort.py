# Selection Sort is a comparison-based sorting algorithm. 
# It sorts an array by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element. 
# This process continues until the entire array is sorted.

# 1. First we find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
# 2. Then we find the smallest among remaining elements (or second smallest) and swap it with the second element.
# 3. We keep doing this until we get all elements moved to correct position.

def selection_sort(arr):
    for i in range(len(arr) - 1):
        idx = i
        for j in range(i + 1, len(arr)):
            if arr[idx] > arr[j]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    
    print("Original array: ", end="")
    print(" ".join(map(str, arr)))
    
    selection_sort(arr)
    
    print("Sorted array: ", end="")
    print(" ".join(map(str, arr)))

    # Complexity Analysis of Selection Sort

    # Time Complexity: O(n2) ,as there are two nested loops:

    # One loop to select an element of Array one by one = O(n)
    # Another loop to compare that element with every other Array element = O(n)
    # Therefore overall complexity = O(n) * O(n) = O(n*n) = O(n2)