from flask import Blueprint, request, jsonify

from settings import TOYS, DEVICES

device = Blueprint("device", __name__)


@device.route("/toy_login", methods=["POST"])
def toy_login():
    device_key = request.form.get("device_key")
    device_info = DEVICES.devices.find_one({"device_key": device_key})
    if device_info:
        toy_info = TOYS.toy.find_one({"device_key": device_key})
        if toy_info:
            return jsonify({"static": "welcome.mp3", "toy_id": str(toy_info.get("_id"))})
        else:
            # 没有绑定用户
            return jsonify({"static": "Nobind.mp3"})

    else:
        # 没有授权
        return jsonify({"static": "Nolice.mp3"})
