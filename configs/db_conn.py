"""
MongoDB database connection file
"""
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB")


def get_database():
    client = MongoClient(MONGO_URL)
    db = client[MONGO_DB]
    return db


print(f"MONGO_URL: {MONGO_URL}")
print(f"MONGO_DB: {MONGO_DB}")
