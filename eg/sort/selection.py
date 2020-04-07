""" 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕
"""

def selectionSort(arr):
  for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
      if arr[min_idx] > arr[j]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
arr = [64, 25, 12, 22, 11]
selectionSort(arr)
print(arr) #[11, 12, 22, 25, 64]

#待排序数组arr，排序方式order>0升序，order<0降序
def selectSort(arr,order):
    rborder = len(arr)
    for i in range(0,rborder):
        p = i
        j = i+1
        while(j<rborder):
            if((arr[p]>arr[j]) and (int(order)>0)) or ((arr[p]<arr[j]) and (int(order)<0)):
                p = j
            j += 1
        arr[i], arr[p] = arr[p], arr[i]
        i += 1
    return arr

A = [64, 25, 12, 22, 11] 
print(selectSort(A, -1))
print(selectSort(A, 1))