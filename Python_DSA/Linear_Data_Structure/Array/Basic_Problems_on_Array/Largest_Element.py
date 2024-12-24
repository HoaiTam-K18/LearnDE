# Given an array arr[] of size n, the task is to find the largest element in the given array

# Input: arr[] = {10, 20, 4}
# Output: 20
# Explanation: Among 10, 20 and 4, 20 is the largest. 


# Input : arr[] = {20, 10, 20, 4, 100}
# Output : 100

def largest(arr):
    mx = arr[0]
    for i in arr:
        if mx < i:
            mx = i
    return mx

if __name__ == "__main__":
    arr = [10, 20, 30, 50, 2, 40]
    mx = largest(arr)
    print("Largest in given array is", mx)

    # Recursive Approach – O(n) Time and O(n) Space
