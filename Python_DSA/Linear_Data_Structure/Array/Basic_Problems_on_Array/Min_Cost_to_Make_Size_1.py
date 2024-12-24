# Given an array of n integers. We need to reduce size of array to one. We are allowed to select a pair of integers and remove the larger one of these two. 
# This decreases the array size by 1. Cost of this operation is equal to value of smaller one. 
# Find out minimum sum of costs of operations needed to convert the array into a single element.

# Input: 4 3 2 
# Output: 4
# Explanation: Choose (4, 2) so 4 is removed, new array = {2, 3}. Now choose (2, 3) so 3 is removed.  So total cost = 2 + 2 = 4

# Input: 3 4
# Output: 3
# Explanation: choose 3, 4, so cost is 3. 

def cost(arr):

    # Minimum cost is n-1 multiplied
    # with minimum element.
    return ( (len(arr) - 1) * min(arr) )


# driver code
arr = [10, 20, 30, 40, 50]
print(cost(arr))