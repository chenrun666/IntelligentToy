from pymongo import MongoClient

db = MongoClient("127.0.0.1", 27017)
COLLECTION = db.ximalaya
USER = db.user
DEVICES = db.devices
TOYS = db.toys
CHAT = db.chat

IMAGE_URL = "image"
AUDIO_URL = "audio"
AVATAR_PATH = "avatar"

# 数据交互协议
RET = {
    "code": 0,
    "msg": "",
    "data": {}
}
