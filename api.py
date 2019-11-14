from flask import Flask
from flask import request
from instapy_cli import client

app = Flask(__name__)

@app.route('/newPost')
def home():
    username = '***'
    password = '***'

    image = request.args['imgSrc']

    text = request.args['postText']

    repsonse = "empty"

    with client(username, password) as cli:
            response = cli.upload(image, text)
    
    return response

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', debug=True)
