from flask import Flask
from flask import jsonify
from flask import request
from logging.config import dictConfig
from flask_cors import CORS
import json

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})



app = Flask(__name__)
CORS(app)

@app.route("/hello", methods=['GET', 'POST'])
def hello_world():
    data = request.json
    print(data)

    urls = ["google","baidu","yahoo"]
    content = {}
    content["urls"] = urls
    jsonifiedContent= jsonify(content)
    print(jsonifiedContent)
    # return "<p>Hello, World!</p>"
    return jsonifiedContent

@app.route("/echoJson", methods=['GET', 'POST'])
def echoJson():
    data = request.json
    # jsonifiedContent = jsonify(data)
    app.logger.info('body content: ' + json.dumps(data))
    return data

@app.route("/echo", methods=['GET', 'POST'])
def echo():
    app.logger.info('text is: ' + request.args.get('text', ''))
    return "You said: " + request.args.get('text', '')

@app.route("/download", methods=['GET', 'POST'])
def downlaod_img():
    url = request.json['urls']
    print(url)
    return "success"
    # img_data = requests.get(image_url).content

