#!/usr/bin/python3
"""
This module use API to export data in the json format
"""
import json
import sys
import urllib.request


if __name__ == '__main__':
    _id = sys.argv[1]
    url_1 = "https://jsonplaceholder.typicode.com/users/{}".format(_id)
    url_2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(_id)
    

    json_info = []

    response = urllib.request.urlopen(url_1)
    data = response.read()
    decoded_data = data.decode('utf-8')
    json_data = json.loads(decoded_data)
    username = json_data.get('username')

    response = urllib.request.urlopen(url_2)
    data = response.read()
    decoded_data = data.decode('utf-8')
    json_data = json.loads(decoded_data)

    for task in json_data:
        dict_data = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": username}
        json_info.append(dict_data)

    d_task = {str(_id): dict_data}

    filename = '{}.json'.format(_id)
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
