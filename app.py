from flask import Flask
import json
import time

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home',
                'Message': 'Loaded Home Page', 'Time': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == '__main__':
    app.run()
