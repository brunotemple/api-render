import json
import time


def pack_fn():
    data_set = {'Page': 'Pack',
                'Message': 'Loaded Pack Page', 'Time': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump
