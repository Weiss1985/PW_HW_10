import configparser
from pymongo import MongoClient

config = configparser.ConfigParser()
config.read('../config.ini')

USER = config.get('DB', 'USER')
PASS = config.get('DB', 'PASS')
DB_NAME = config.get('DB', 'DB_NAME')
DOMAIN = config.get('DB', 'DOMAIN')


def get_mongodb():
    # client = MongoClient("mongodb+srv://weiss1985:Q!w2e3r4t5@weiss-pw-hw.pdwaq7b.mongodb.net/?retryWrites=true&w=majority")
    client = MongoClient(f"mongodb+srv://{USER}:{PASS}@{DOMAIN}.pdwaq7b.mongodb.net/?retryWrites=true&w=majority")
    db = client.book
    return db



