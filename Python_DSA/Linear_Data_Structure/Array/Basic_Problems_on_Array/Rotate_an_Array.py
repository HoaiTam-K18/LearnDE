# Let us take arr[] = {1, 2, 3, 4, 5, 6}, d = 2.


# First Step:
#         => Rotate to right by one position.
#         => arr[] = {6, 1, 2, 3, 4, 5}
# Second Step:
#         => Rotate again to right by one position
#         => arr[] = {5, 6, 1, 2, 3, 4}
# Rotation is done 2 times.
# So the array becomes arr[] = {5, 6, 1, 2, 3, 4}

def rotateArr(arr, d):
    if d % len(arr) == 0:
        return arr

    d = d % len(arr)
    res = []

    res.extend(arr[0-d:])

    for i in range(0, len(arr) - d, 1):
        res.append(arr[i])

    for i in range(len(res)):
        arr[i] = res[i]
    
        


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    d = 5
    rotateArr(arr, d)
    print(" ".join(map(str, arr)))