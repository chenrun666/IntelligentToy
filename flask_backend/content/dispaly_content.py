import os

from flask import Blueprint, jsonify, send_file, request
from bson import ObjectId

from settings import COLLECTION
from settings import AVATAR_PATH
from settings import USER
from settings import TOYS
from settings import RET

content = Blueprint("content", __name__)


@content.route("/content_list", methods=["POST"])
def content_list():
    content_lists = list(COLLECTION.data.find({}))
    for index, item in enumerate(content_lists):
        content_lists[index]["_id"] = str(content_lists[index]["_id"])
    return jsonify(content_lists)


@content.route("/avatar/<gender>")
def get_avatar(gender):
    avatar_path = os.path.join(AVATAR_PATH, gender)
    return send_file(avatar_path)


@content.route("/my_toy", methods=["POST"])
def get_my_toy():
    user_id = request.form.get("user_id")

    user_info = USER.userinfo.find_one({"_id": ObjectId(user_id)})
    toy_list = user_info.get("bind_toy")
    for index, item in enumerate(toy_list):  # [4234234, 42324342]
        toy_list[index] = ObjectId(item)  # 换成ObjectId匹配对应的玩具

    bind_toy = list(TOYS.toy.find({"_id": {"$in": toy_list}}))

    for index, item in enumerate(bind_toy):
        bind_toy[index]["_id"] = str(bind_toy[index]["_id"])

    RET["code"] = 0
    RET["msg"] = "获取成功"
    RET["data"] = bind_toy

    return jsonify(RET)


@content.route("/get_qr/<device_id>")
def get_qr(device_id):
    path = f"{os.path.join('QRCode/QR_images', device_id)}.jpg"
    return send_file(path)
