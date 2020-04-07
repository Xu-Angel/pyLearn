""" 以中间为基准 """
def quickSort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  right = [x for x in arr if x > pivot]
  middle = [x for x in arr if x == pivot]
  return quickSort(left) + middle + quickSort(right)
print(quickSort([3, 6, 8, 19, 1, 5]))  # [1, 3, 5, 6, 8, 19]

""" 以最后一个作为基准值 """
def quickSort(aList):
    if len(aList) <= 1:
        return aList
    # pivot = aList[len(aList)-1]
    pivot = -1
    for index,item in enumerate(aList):
        if item < pivot:
            pivot += 1
            aList[pivot], aList[index] = aList[index], aList[pivot]
    pivot = pivot + 1
    aList[pivot], aList[index] = aList[index], aList[pivot]
   # left = quickSort(aList[:pivot]) 
    quickSort(aList[:pivot]) 
   # middle = [aList[pivot]]
   # right = quickSort(aList[pivot+1:])
    quickSort(aList[pivot+1:])
    #newList = left+middle+right
    # return newList

theList = [123,45,32,555,64,31,45,50,658,55,1,45]
quickSort(theList)
print(theList)