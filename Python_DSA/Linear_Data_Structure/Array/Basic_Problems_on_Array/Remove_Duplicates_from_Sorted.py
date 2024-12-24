# Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. 
# Additionally, return the length of this distinct sorted subarray.

# Note: The elements after the distinct ones can be in any order and hold any value, as they don’t affect the result.

# Input: arr[] = [2, 2, 2, 2, 2]
# Output: [2]
# Explanation: All the elements are 2, So only keep one instance of 2.


# Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5, 5]
# Output: [1, 2, 3, 4, 5]

# Input: arr[] = [1, 2, 3]
# Output: [1, 2, 3]
# Explanation : No change as all elements are distinct.


def removeDuplicates(arr):
    res = []
    idx = None

    for i in arr:
        if not res:
            res.append(i)
            idx = i
        else:
            if idx != i:
                res.append(i)
                idx = i
    return res


if __name__ == "__main__":
    arr = [10, 20, 20, 30, 40, 50]
    new_arr = removeDuplicates(arr)
    print(" ".join(map(str, new_arr)))