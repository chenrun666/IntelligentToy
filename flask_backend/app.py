from flask import Flask, jsonify, render_template

from content import dispaly_content
from content import get_audio_image
from content import user

app = Flask(__name__)

app.register_blueprint(dispaly_content.content)
app.register_blueprint(get_audio_image.getdata)
app.register_blueprint(user.user)


@app.route("/toy")
def toy():
    return render_template("toy.html")


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
