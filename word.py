# encoding=utf-8
import jieba

# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
with open("word.txt", 'r', encoding='utf-8') as f:
  strr = f.read()

seg_list = jieba.cut(strr, cut_all=False)
# print (next(seg_list), end="")  # "Default Mode: " 精确模式

# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))

str = ", ".join(seg_list)
data = open("out.txt", 'w+', encoding='utf-8')
print(str.split(','), file=data)
data.close()

# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))