# 一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。
import support

# 例如，要导入模块 fib 的 fibonacci 函数，使用如下语句：
# form fib import fibonacci
# 这个声明不会把整个 fib 模块导入到当前的命名空间中，它只会将 fib 里的 fibonacci 单个引入到执行这个声明的模块的全局符号表。


support._print('ss')