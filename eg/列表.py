
""" 
最小元素
 """
list1 = [10, 20, 4, 45, 99] 
  
list1.sort() 
  
print("最小元素为:", list1[:1], *list1[:1], min(list1))

""" 
清空列表
 """
# list1.clear()


""" 
复制列表
 """
# list1[:]

# [].extend(list1)

# list(list1)

""" 
元素之和
 """

total = 0
  
list1 = [11, 5, 17, 18, 23]  

for key in range(0, len(list1)):
  total = total + list1[key]

# ----
total = 0
  
list1 = [11, 5, 17, 18, 23]  
key = 0
while (key < len(list1)):
  total = total + list1[key]
  key += 1
  
#---
list1 = [11, 5, 17, 18, 23]

def sumByRecursion(list, size):
  if (size == 0):
    return 0
  else:
    return sumByRecursion(list, size - 1) + list[size - 1]

print(sumByRecursion(list1, len(list1)))