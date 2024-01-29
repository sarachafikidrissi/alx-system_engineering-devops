#!/usr/bin/python3
"""
This module use API to return information
of a given employee
"""
import json
import sys
import urllib.request


if __name__ == '__main__':
    _id = sys.argv[1]
    url_1 = "https://jsonplaceholder.typicode.com/users/{}".format(_id)
    url_2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(_id)

    response = urllib.request.urlopen(url_1)
    data = response.read()
    decoded_data = data.decode('utf-8')
    json_data = json.loads(decoded_data)

    name = json_data.get('name')

    print("Employee {} is done with tasks".format(name), end="")

    response = urllib.request.urlopen(url_2)
    data = response.read()
    decoded_data = data.decode('utf-8')
    tasks = json.loads(decoded_data)

    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("({}/{}):".format(done, len(tasks)))

    for n in done_tasks:
        print("\t {}".format(n.get('title')))
