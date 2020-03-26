#https://www.runoob.com/python3/python3-list-operator.html
li = ['a', 'b', 'mpilgrim', 'z', 'example']
print(li[-3])
print(li[3])
print(li[0:3])
print(li[1:-1])# [:] 这种包前不包后[)
li.insert(2, 'new')
print(li)
li.extend(['two', 'elements'])
print(li)
print(li.index("new")) # 查询val的index
li.remove('z')  # # 删除首次出现的一个值
print(li)
li.pop()  # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
print(li)

# +  可以直接连接两个list 形成新的list

lic = ['a', 'b', 'mpilgrim', 'example', 'new']
lic = lic + ['example', 'new']
print(lic)

# list转字符串
# join 只能用于元素是字符串的 list; 它不进行任何的类型强制转换。连接一个存在一个或多个非字符串元素的 list 将引发一个异常。
params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
print(";".join(["%s=%s" % (k, v) for k, v in params.items()]))