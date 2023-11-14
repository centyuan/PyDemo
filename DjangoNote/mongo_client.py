from pymongo import MongoClient

my_client = MongoClient("mongodb://localhost:27017/")
my_db = my_client["fuzhen"]
my_col = my_db['apk']

