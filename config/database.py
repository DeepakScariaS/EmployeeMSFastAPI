from pymongo import MongoClient

client = MongoClient("mongodb+srv://root:admin@cluster0.5nzqe2m.mongodb.net/?retryWrites=true&w=majority")

db = client.emp_db

collection_name = db["employee_collection"]