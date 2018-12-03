from flask import jsonify
from flask import Blueprint
from flask import request

from settings import USER
from settings import RET

user = Blueprint("user", __name__)


@user.route("/reg", methods=["POST"])
def reg_func():
    username = request.form.get("username")
    password = request.form.get("password")
    gender = request.form.get("gender")
    nickname = request.form.get("nickname")

    db_username = USER.userinfo.find_one({"username": username})

    if db_username:
        RET["code"] = 1
        RET["msg"] = "用户名已存在"
        RET["data"] = {}

        return jsonify(RET)

    user = {
        "username": username,
        "password": password,
        "gender": int(gender),
        "nickname": nickname,
        "avatar": "girle.jpg" if gender == 0 else "boy.jpg",
        "bind_toy": [],
        "friend_list": [],
    }
    USER.userinfo.insert_one(user)

    RET["code"] = 0
    RET["msg"] = "注册成功"
    RET["data"] = {}

    return jsonify(RET)


@user.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "" and password == "":
        RET["code"] = 1
        RET["msg"] = "用户名密码不能为空"
        RET["data"] = []

        return jsonify(RET)

    user_obj = USER.userinfo.find_one({"username": username, "password": password})
    user_obj["_id"] = str(user_obj["_id"])
    if user_obj:
        RET["code"] = 0
        RET["msg"] = "登陆成功"
        RET["data"] = user_obj

    else:
        RET["code"] = 2
        RET["msg"] = "用户名密码错误"
        RET["data"] = []

    return jsonify(RET)
