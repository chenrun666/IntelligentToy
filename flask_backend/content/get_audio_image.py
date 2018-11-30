import os

from flask import Blueprint, send_file
from settings import IMAGE_URL
from settings import AUDIO_URL

getdata = Blueprint("getdata", __name__)


@getdata.route("/get_image/<filename>")
def get_image(filename):
    content_file = os.path.join(IMAGE_URL, filename)
    return send_file(content_file)


@getdata.route("/get_audio/<filename>")
def get_audio(filename):
    content_file = os.path.join(AUDIO_URL, filename)
    return send_file(content_file)
