import pymongo
import os
if os.path.exists('env.py'):
    import env


def mongo_connect():
    MONGODB_URI = os.environ.get('MONGODB_URI')
    DBS_NAME = os.environ.get('DBS_NAME')
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME')
    conn = pymongo.MongoClient(MONGODB_URI)
    coll = conn[DBS_NAME][COLLECTION_NAME]
    return coll

