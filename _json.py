import json
dataJ = [{'a':1, 'b':2, 'c':3, 'd':4, 'e':5}]
print(json.dumps(dataJ))
print(json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': ')))

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

text = json.loads(jsonData)

print(text)