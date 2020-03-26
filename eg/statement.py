# if num> = 0:
# num = float(input('please input a number:'))
# if num == 0:
#   print('result = 0')
# else:
#   if num < 0:
#     print('result < 0')
#   else:
#     print('result > 0')

# 每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
# 使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
# py用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
# py没有switch语句

age = int(input("请输入狗狗的年龄："))
print("")
if age <= 0:
  print("???")
elif age == 1:
  print("相当于人类14岁")
elif age == 2:
  print("相当于人类22岁")
elif age > 2:
  human = 22 + (age - 2) * 5
  print('对应人类年龄：', human)

# while 判断条件(condition)：
#   执行语句(statements)……
# Python 中没有 do..while 循环。

n = 100
 
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n, sum))

""" while 循环使用 else 语句
在 while … else 在条件语句为 false 时执行 else 的语句块。 """
count =0
while count< 5:
  print(count, "小于5")
  count = count + 1
else:
  print(count, "大于等于5")

# 类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：
flag = 1
while (flag == 1 ): print('hello')
print("bye")

 
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
  print(i, a[i])

""" break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。

continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。 """