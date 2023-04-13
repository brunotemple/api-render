from flask import Flask
import json
import time
from lib.pack import pack_fn

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home',
                'Message': 'Loaded Home Page', 'Time': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/pack', methods=['GET'])
def pack_page():
    json_dump = pack_fn()

    return json_dump


if __name__ == '__main__':
    app.run()
