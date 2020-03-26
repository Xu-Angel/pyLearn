a = {'坚守', ' 传统', ' 婚姻家庭', ' 观念', ' 的', ' 人', ' 人', ' 身体健康'}
print(a)
print(list(a))
seta = set('abracadabra')
setb = set('alacazam')
print(seta - setb)# 在 a 中的字母，但不在 b 中
print(seta | setb)
print(seta & setb)
print(seta ^ setb)  # 在 a 或 b 中的字母，但不同时在 a 和 b 中
print({x for x in 'abracadabra' if x not in 'abc'}) # 推导式