from flask import Flask
from flask import request
from instapy_cli import client
import json

app = Flask(__name__)

@app.route('/newPost')
def home():
    username = '***'
    password = '***'

    image = request.args.get("imgSrc", "NO_IMAGE_DEFINED")

    text = request.args.get("postText", "NO_TEXT_DEFINED")

    postOnStory = request.args.get("postOnStory",False) == 'True'

    repsonse = {}
    repsonse["imgSrc"] = image
    repsonse["postText"] = text
    repsonse["postOnStory"] = postOnStory

    with client(username, password) as cli:
        result = None
        if postOnStory:
            result = cli.upload(image, story=True)
        else:
            result = cli.upload(image, text)

        if result == None:
            repsonse["msg"] = "Upload was not successfull"
        else:
            repsonse["msg"] = "Upload successfull"

    return json.dumps(repsonse)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
