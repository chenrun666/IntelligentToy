from bson import ObjectId
from flask import Blueprint, request, jsonify

from settings import TOYS
from settings import RET

friend = Blueprint("friend", __name__)


@friend.route("/get_friend", methods=["POST"])
def get_friend():
    toy_id = request.form.get("toy_id")
    toy_info = TOYS.toy.find_one({"_id": ObjectId(toy_id)})

    RET["code"] = 0
    RET["msg"] = "查询好友成功"
    RET["data"] = toy_info

    return jsonify(RET)
