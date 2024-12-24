# You are given an array of n-elements, you have to find the number of operations needed to make all elements of array equal. 
# Where a single operation can increment an element by k. If it is not possible to make all elements equal print -1

# Input : arr[] = {4, 7, 19, 16},  k = 3
# Output : 10

# Input : arr[] = {4, 4, 4, 4}, k = 3
# Output : 0

# Input : arr[] = {4, 2, 6, 8}, k = 3
# Output : -1

def minOps(arr, k):
    mx = max(arr)
    count = 0

    for i in arr:
        while i < mx:
            i += k
            count += 1
        if i != mx:
            return -1
    return count


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    k = 10
    print(minOps(arr, k))