# Given an array arr[] of size n, the task is to find all the Leaders in the array. An element is a Leader if it is greater than or equal to all the elements to its right side.

# Note: The rightmost element is always a leader.

# Input: arr[] = [16, 17, 4, 3, 5, 2]
# Output: [17 5 2]
# Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2], therefore 17 is a leader. 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.


# Input: arr[] = [1, 2, 3, 4, 5, 2]
# Output: [5 2]
# Explanation: 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

# Function to find the leaders in an array
def leaders1(arr):
    res = []
    n = len(arr)
    
    for i in range(n):
        # Check elements to the right
        for j in range(i + 1, n):
            # If a larger element is found
            if arr[i] < arr[j]:
                break
        else:
            # If no larger element was found
            res.append(arr[i])
    return res

def leaders2(arr):
    res = []

    # Start with the rightmost element
    maxRight = arr[-1]
    # Rightmost element is always a leader
    res.append(maxRight)

    # Traverse the array from right to left
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > maxRight:
            maxRight = arr[i]
            res.append(maxRight)
            
    # Reverse the result list to maintain
    # original order       
    res.reverse()
    return res

if __name__ == "__main__":
    arr = [10, 30, 50, 40, 20]
    res = leaders1(arr)
    print(" ".join(map(str, res)))

    res = leaders2(arr)
    print(" ".join(map(str, res)))

    range

