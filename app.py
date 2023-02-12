import requests
import json
from flask import Flask, render_template

app = Flask(__name__)


def get_list_of_items():
    url = "https://simulith.space/api/storage/all"
    response = json.loads(requests.request("GET", url).text)
    return response


@app.route("/")
def index():
    items = get_list_of_items()
    return render_template('index.html', items=items)


if __name__ == '__main__':
    app.run()
