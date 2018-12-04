from flask import request, jsonify
from flask import Blueprint
from bson import ObjectId

from settings import USER
from settings import DEVICES
from settings import RET
from settings import TOYS
from settings import CHAT

valid = Blueprint("valid", __name__)


@valid.route("/valid/", methods=["POST"])
def valid_code():
    valid_code = request.form.get("code")
    code_obj = DEVICES.devices.find_one({"device_key": valid_code})
    if code_obj:
        print(code_obj)
        RET["code"] = 0
        RET["msg"] = "验证通过, 进入绑定流程～～～"
        RET["data"] = {"device": valid_code}
        return jsonify(RET)

    RET["code"] = 2
    RET["msg"] = "验证失败，请联系生产厂家"
    RET["data"] = {}

    return jsonify(RET)


@valid.route("/bindtoy/", methods=["POST"])
def bind_toy():
    toyname = request.form.get("toyname")
    name = request.form.get("name")
    talkname = request.form.get("talkname")
    gender = request.form.get("gender")
    device_key = request.form.get("device_key")
    user_id = request.form.get("user_id")

    chat_window = CHAT.chat.insert_one({"user_list": [], "chat_list": []})
    userinfo = USER.userinfo.find_one({"_id": ObjectId(user_id)})

    create_toy = {
        "device_key": device_key,
        "toyname": toyname,
        "name": name,
        "avatar": "body.jpg" if gender == 1 else "girle.jpg",
        "bind_user": str(userinfo.get("_id")),
        "friend_list": [
            {
                "friend_nickname": userinfo.get("nickname"),
                "friend_remark": talkname,
                "friend_id": str(userinfo.get("_id")),
                "friend_avatar": userinfo.get("avatar"),
                "friedn_chat": str(chat_window.inserted_id),
            }
        ]

    }

    toy = TOYS.toy.insert_one(create_toy)

    userinfo["bind_toy"].append(str(toy.inserted_id))
    userinfo["friend_list"].append(
        {
            "friend_nickname": create_toy.get("name"),
            "friend_remark": create_toy.get("toyname"),
            "friend_id": str(toy.inserted_id),
            "friend_avatar": create_toy.get("avatar"),
            "friedn_chat": str(chat_window.inserted_id),
        }
    )

    USER.userinfo.update_one({"_id": ObjectId(user_id)}, {"$set": userinfo})

    user_list = [str(userinfo.get("_id")), str(toy.get("_id"))]
    CHAT.chat.update_one({"_id": chat_window.inserted_id}, {"$set": {"user_list": user_list}})

    RET["code"] = 0
    RET["msg"] = "玩具绑定成功"
    RET["data"] = {}

    return jsonify(RET)
