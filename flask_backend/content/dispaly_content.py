import os

from flask import Blueprint, jsonify, send_file

from settings import COLLECTION
from settings import AVATAR_PATH

content = Blueprint("content", __name__)


@content.route("/content_list", methods=["POST"])
def content_list():
    content_list = list(COLLECTION.data.find({}))
    for index, item in enumerate(content_list):
        content_list[index]["_id"] = str(content_list[index]["_id"])
    return jsonify(content_list)


@content.route("/avatar/<gender>")
def get_avatar(gender):
    avatar_path = os.path.join(AVATAR_PATH, gender)
    print(avatar_path)
    return send_file(avatar_path)



