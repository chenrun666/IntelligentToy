import json
import uuid

import requests

from settings import COLLECTION

"""
1， 获取href=/ertong/424529/7713768, 最后的数字，与http://m.ximalaya.com/tracks/，拼接
2， 访问的url：http://m.ximalaya.com/tracks/7713678.json
3， 获取到一个json的数据，提取自己想要的数据
"""


# 获取图片和音频的函数，并且构建字典放到mongodb中
def get_image_audio(url, data_info):
    for res in data_info:
        filename = uuid.uuid4()
        res_url = url + res + ".json"
        res_dic = json.loads(requests.get(res_url).content.decode("utf-8"))

        # 构建字典
        result_dic = {
            "audio": "",
            "cover": "",
            "title": res_dic.get("title"),
            "album_title": res_dic.get("album_title"),
            "nickname": res_dic.get("nickname"),
        }
        image_url = res_dic.get("cover_url")
        audio_url = res_dic.get("play_path")

        image = requests.get(image_url)
        audio = requests.get(audio_url)

        # 写入到文件中
        with open(f"../image/{filename}.jpg", "wb") as f:
            f.write(image.content)

        with open(f"../audio/{filename}.mp3", "wb") as f:
            f.write(audio.content)

        result_dic["audio"] = f"{filename}.mp3"
        result_dic["cover"] = f"{filename}.jpg"

        # 保存到mongodb中
        COLLECTION.data.insert_one(result_dic)


if __name__ == '__main__':
    base_url = "http://m.ximalaya.com/tracks/"
    data_info = ["7713768", "7713564",
                 "7713762", "7713682"]
    get_image_audio(base_url, data_info)
