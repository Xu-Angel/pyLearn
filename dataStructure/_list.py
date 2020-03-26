# Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。
a = ['坚守', ' 传统', ' 婚姻家庭', ' 观念', ' 的', ' 人', ' 人', ' 身体健康']
b = []
print([ {'word': i, 'count': a.count(i)}for i in a]) # 简写
for i in a:
  b.append({"word": i, 'count': a.count(i)})
print(b)
# 堆栈 ：最先进入的元素最后一个被释放（后进先出）。用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。例如：

# 队列
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
#'Eric'
queue.popleft()                 # The second to arrive now leaves
#'John'
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

# 推导式
vec = [2,4,6]
print([3 * x for x in vec])
print([[x, x ** 2] for x in vec])
print([3*x for x in vec if(x > 3)]) # 过滤器
#对序列里每一个元素逐个调用某方法：
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
  transposed.append([row[i] for row in matrix])
print(transposed)

_transposed = []
for i in range(4):
  transposed_row = []
  for row in matrix:
    transposed_row.append(row[i])
  _transposed.append(transposed_row)
print(_transposed)

# 使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，或清空整个列表
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
# [1, 66.25, 333, 333, 1234.5]
del a[2:4]
# [1, 66.25, 1234.5]
del (a[:])
# []