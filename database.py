#coding=utf-8
# import pymongo
from pymongo import MongoClient
# /girldatabasev1-1?authSource=admin
client = MongoClient('mongodb://root:password123@123.207.72.208:27017')
db = client['girldatabasev1-1']
collection = db.allgirls
st = collection.find_one({'area': '广东'})
data = open("out1.txt", 'w+', encoding='utf-8')
print(st, file=data)
data.close()
print(st)
