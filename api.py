from flask import Flask
from flask import request
from instapy_cli import client
import json
import random

app = Flask(__name__)

@app.route('/newPost')
def home():
    useFakeAccount = request.args.get("useFakeAccount", False) == 'True'

    username = '***'
    password = '***'

    if useFakeAccount:
        username = '***'
        password = '***'

    image = request.args.get("imgSrc", "NO_IMAGE_DEFINED") #Image Path

    text = request.args.get("postText", "NO_TEXT_DEFINED") #Post Description

    #Post on Story? If you post on Story than your provided text is ignored
    postOnStory = request.args.get("postOnStory",False) == 'True'
    
    #Fake Post? If True the post will not be commited to Instagram
    isFakePost = request.args.get("isFakePost", False) == 'True'

    response = {}
    response["imgSrc"] = image
    response["postText"] = text
    response["postOnStory"] = postOnStory
    response["posted"] = False

    if isFakePost == False:
        with client(username, password) as cli:
            result = None
            if postOnStory:
                result = cli.upload(image, story=True)
            else:
                result = cli.upload(image, text)

            if result == None:
                response["msg"] = "Upload was not successfull"
            else:
                response["msg"] = "Upload successfull"
                response["posted"] = True
    else:
        if random.random() < .5:
            response["posted"] = True
        response["msg"] = "This was a fake Post"

    return json.dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
