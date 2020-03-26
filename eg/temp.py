# 交换变量
a = 1
b = 2
temp = a
a = b
b = temp
print(a, b)

# 不创建temp

c = 4
d = 5
c,d = d,c
print(c, d)

# 异或
x = 8
y = 10
x = x ^ y
y = x ^ y
x = x ^ y

print(x, y)