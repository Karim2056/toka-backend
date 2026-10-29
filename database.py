from pymongo import MongoClient

#connection to db
client = MongoClient("mongodb://localhost:27017")

#stating which dbs we are using
db = client["toka_fitness"]

#getting specific collections we have, so other files can import and use them

users = db["users"]

users.create_index("email", unique=True)