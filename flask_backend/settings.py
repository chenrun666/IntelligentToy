from pymongo import MongoClient

db = MongoClient("127.0.0.1", 27017)
COLLECTION = db.ximalaya

IMAGE_URL = "image"
AUDIO_URL = "audio"
