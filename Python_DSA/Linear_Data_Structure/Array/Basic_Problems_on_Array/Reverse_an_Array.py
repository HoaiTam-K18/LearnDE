# Given an array arr[], the task is to reverse the array. 
# Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.

# Input: arr[] = {1, 4, 3, 2, 6, 5}  
# Output: {5, 6, 2, 3, 4, 1}
# Explanation: The first element 1 moves to last position, the second element 4 moves to second-last and so on.


# Input: arr[] = {4, 5, 1, 2} 
# Output: {2, 1, 5, 4}
# Explanation: The first element 4 moves to last position, the second element 5 moves to second last and so on.

def reverseArray1(arr):
    res = []
    for i in range(len(arr) - 1, -1, -1):
        res.append(arr[i])
    
    return res

def reverseArray2(arr):
    temp = []
    for i in range(len(arr) - 1, -1, -1):
        temp.append(arr[i])
    
    for i in range(len(arr)):
        arr[i] = temp[i]

    


if __name__ == "__main__":
    arr  =  [10, 20, 30, 40, 50]
    
    new_arr  = reverseArray1(arr)
    print(" ".join(map(str, new_arr)))

    reverseArray2(arr)
    print(" ".join(map(str, arr)))