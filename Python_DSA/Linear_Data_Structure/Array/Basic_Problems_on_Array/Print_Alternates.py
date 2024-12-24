# Given an array arr[], the task is to print every alternate element of the array starting from the first element.

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: 10 30 50
# Explanation: Print the first element (10), skip the second element (20), print the third element (30), skip the fourth element(40) and print the fifth element(50).


# Input: arr[] = [-5, 1, 4, 2, 12]
# Output: -5 4 12

def getAlternates1(arr):
    res = []

    for i in range(0, len(arr), 2):
        res.append(arr[i])

    return res

def getAlternatesByRec(arr, index, res):
    if index < len(arr):
        res.append(arr[index])
        return getAlternatesByRec(arr, index + 2, res)

def getAlternates2(arr):
    res = []
    getAlternatesByRec(arr, 0, res)
    return res


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    res = getAlternates1(arr)
    print(" ".join(map(str, res)))

    # Time Complexity: O(n), where n is the number of elements in arr[].
    # Auxiliary Space: O(1)

    res = getAlternates2(arr)
    print(" ".join(map(str, res)))

    # Time Complexity: O(n), where n is the number of elements in arr[].
    # Auxiliary Space: O(n), for recursive call stack.
