def Merge(dict1, dict2):
  return (dict2.update(dict1))  # update() 方法，第二个参数合并第一个参数

def Merge(dict1, dict2):
  return ({**dict1, **dict2}) # 使用 **，函数将参数以字典的形式导入