from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

result = db.movies.find_one({'title' : '월-E'})
print(result['star'])



db.movies.update_many({'star': result['star']},{'$set':{'star': 0}})