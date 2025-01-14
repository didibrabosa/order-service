"""
MongoDB database connection file
"""

import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def get_database_connection():
    """
    Establishes and returns a connection to the MongoDB database.
    """
    db_host = os.getenv("DATABASE_HOST", "localhost")
    db_port = int(os.getenv("DATABASE_PORT", 27017))
    db_name = os.getenv("DATABASE_NAME", "orders")

    client = MongoClient(host=db_host, port=db_port)

    return client[db_name]
