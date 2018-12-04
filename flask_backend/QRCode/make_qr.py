import os
import time
import uuid
import hashlib

import qrcode

from settings import DEVICES


def create_qr(count):
    qr_list = []

    for num in range(count):
        device_key = f"{uuid.uuid4()}{time.time()}{uuid.uuid4()}"
        device_key = hashlib.md5(device_key.encode("utf-8")).hexdigest()

        qr_obj = qrcode.make(device_key)
        qr_path = f"{os.path.join('QR_images', device_key)}.jpg"
        qr_obj.save(qr_path)

        qr_list.append({"device_key": device_key})

    DEVICES.devices.insert_many(qr_list)


create_qr(5)
