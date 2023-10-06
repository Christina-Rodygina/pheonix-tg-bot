from flask import Flask
from core.handlers.notifications import notification
from flask import request

app = Flask(__name__)


@app.route("/")
async def hello():
    key_request = request.get_json()['key']
    text_request = request.get_json()['text']
    await notification(key_request, text_request)

    return "<h1>Hello World!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
