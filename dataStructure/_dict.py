""" 字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。

理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。

一对大括号创建一个空的字典：{}。 """

tel = {'jack': 4098, 'sape': 4139}
tel['manny'] = 8888
print(tel)
del tel['sape']
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print('guido' not in tel)
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print({x: x ** 2 for x in (2, 4, 6)})
print(dict(sape=4139, guido=4127, jack=4098))
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
  print(k, v)
for i, v in enumerate(['tic', 'tac', 'toe']):
  print(i, v)
  
  
#要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
  print(f)
#同时遍历两个或更多的序列，可以使用 zip() 组合：

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
  print('What is your {0}?  It is {1}.'.format(q, a))