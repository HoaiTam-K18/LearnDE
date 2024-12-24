# Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. 
# It is like sorting playing cards in your hands. You split the cards into two groups: the sorted cards and the unsorted cards. 
# Then, you pick a card from the unsorted group and put it in the right place in the sorted group.

# We start with second element of the array as first element in the array is assumed to be sorted.
# Compare second element with the first element and check if the second element is smaller then swap them.
# Move to the third element and compare it with the first two elements and put at its correct position
# Repeat until the entire array is sorted.

def insertionSort(arr):
    for i in range(1, len(arr)):
        idx = i - 1
        key = arr[i]
        while idx >= 0 and arr[idx] > key:
            arr[idx + 1] = arr[idx]
            idx -= 1
        arr[idx + 1] = key

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    print(" ".join(map(str, arr)))

    # Complexity Analysis of Insertion Sort
    # Time Complexity of Insertion Sort
    # Best case: O(n) , If the list is already sorted, where n is the number of elements in the list.
    # Average case: O(n 2 ) , If the list is randomly ordered
    # Worst case: O(n 2 ) , If the list is in reverse order

    # Space Complexity of Insertion Sort

    # Auxiliary Space: O(1), Insertion sort requires O(1) additional space, making it a space-efficient sorting algorithm.