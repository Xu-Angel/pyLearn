# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

# Python允许你同时为多个变量赋值。例如：

a = b = c = 1
# 以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。

# 您也可以为多个对象指定多个变量。例如：

a, b, c = 1, 2, "runoob"
# 以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。

# !List（列表） 是 Python 中使用最频繁的数据类型。 与Python字符串不一样的是，列表中的元素是可以改变的：

# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。

# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

# 列表截取的语法格式如下：

# 变量[头下标:尾下标]

list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
 
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print(list + tinylist)  # 连接列表

# Tuple（元组）
# !元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。可以把字符串看作一种特殊的元组。

# 元组中的元素类型也可以不相同：

 
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
 
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print(tuple + tinytuple)  # 连接元组


# string、list 和 tuple 都属于 sequence（序列）。

# 注意：

# 1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法一样。
# 3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
# 4、元组也可以使用+操作符进行拼接。

# Set（集合）
# !集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。

# 基本功能是进行成员关系测试和删除重复元素。

# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# 创建格式：

# parame = {value01,value02,...}
# 或者
# set(value)
 
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
 
print(student)   # 输出集合，重复的元素被自动去掉
 
# 成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
 
 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
 
print(a)
 
print(a - b)     # a 和 b 的差集
 
print(a | b)     # a 和 b 的并集
 
print(a & b)     # a 和 b 的交集
 
print(a ^ b)  # a 和 b 中不同时存在的元素

# Dictionary（字典）
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。

# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

# 键(key)必须使用不可变类型。

# 在同一个字典中，键(key)必须是唯一的。

 
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
 
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
 
 
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print(tinydict.values())  # 输出所有值


# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。