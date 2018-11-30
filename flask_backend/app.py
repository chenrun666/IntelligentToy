from flask import Flask, jsonify

from content import dispaly_content
from content import get_audio_image

app = Flask(__name__)

app.register_blueprint(dispaly_content.content)
app.register_blueprint(get_audio_image.getdata)

if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
