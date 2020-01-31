from flask import Flask
from flask import Response
import urllib.request
import json
import time


AWS_URL = 'https://ip-ranges.amazonaws.com/ip-ranges.json'

def parse_json():
    with urllib.request.urlopen(AWS_URL) as response:
        html = response.read()
    url_list = json.loads(html)
    urls = ""
    for ip in url_list['prefixes']:
        urls += ip['ip_prefix']+"\n"
    return urls


app = Flask(__name__)

@app.route('/')
def index():
    r = Response(parse_json(), status=200, mimetype="application/xml")
    r.headers["status"] = "200"
    r.headers["Content-Type"] = "text; charset=utf-8"
    r.headers["x-powered-by"] = "python script"
    return r

