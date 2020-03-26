def is_number(s):
  try:# 如果能运行float(s)语句，返回True（字符串s是浮点数）
    float(s)
    return True
  except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
      pass# 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
  try:
    import unicodedata # 处理ASCii码的包
    for i in s:
      unicodedata.numeric(i) # 把一个表示数字的字符串转换为浮点数返回的函数
    return True
  except (TypeError, ValueError):
      pass
  return False

  # 测试字符串和数字
print(is_number('foo'))   # False
print(is_number('1'))     # True
print(is_number('1.3'))   # True
print(is_number('-1.37')) # True
print(is_number('1e3'))   # True
 
# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒的'))  # True
# 中文数字
print(is_number('四的')) # True
# 版权号
print(is_number('©'))  # False

def is_leap_year(y):
  if (y % 4) == 0:
    if (y % 100) == 0:
      if (y % 400) == 0:
        print("{0} 是闰年".format(y))
      else:
        print("{0} 不是闰年".format(y))
    else:
      print("{0} 是闰年".format(y))
  else:
    print("{0} 是闰年".format(y))

is_leap_year(2000)
is_leap_year(2011)

""" 
匿名函数
python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
 """

sum = lambda arg1, arg2: arg1 + arg2
print(sum(10,20))