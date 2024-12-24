# Here’s a step-by-step explanation of the cycle sort algorithm:
# Start with an unsorted array of n elements.
# Initialize a variable, cycleStart, to 0.
# For each element in the array, compare it with every other element to its right. If there are any elements that are smaller than the current element, increment cycleStart.
# If cycleStart is still 0 after comparing the first element with all other elements, move to the next element and repeat step 3.
# Once a smaller element is found, swap the current element with the first element in its cycle. 
# The cycle is then continued until the current element returns to its original position.

def cycleSort(array):
  writes = 0
   
  # Loop through the array to find cycles to rotate.
  for cycleStart in range(0, len(array) - 1):
    item = array[cycleStart]
     
    # Find where to put the item.
    pos = cycleStart
    for i in range(cycleStart + 1, len(array)):
      if array[i] < item:
        pos += 1
     
    # If the item is already there, this is not a cycle.
    if pos == cycleStart:
      continue
     
    # Otherwise, put the item there or right after any duplicates.
    while item == array[pos]:
      pos += 1
    array[pos], item = item, array[pos]
    writes += 1
     
    # Rotate the rest of the cycle.
    while pos != cycleStart:
       
      # Find where to put the item.
      pos = cycleStart
      for i in range(cycleStart + 1, len(array)):
        if array[i] < item:
          pos += 1
       
      # Put the item there or right after any duplicates.
      while item == array[pos]:
        pos += 1
      array[pos], item = item, array[pos]
      writes += 1
   
  return writes      


if __name__ == "__main__":
    arr = [1, 8, 3, 9, 10, 10, 2, 4 ]
    cycleSort(arr)
    
    print("After sort :", " ".join(map(str, arr)))
