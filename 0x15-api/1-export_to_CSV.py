#!/usr/bin/python3
"""
This module use API to export data in the CSV format
"""
import csv
import json
import sys
import urllib.request


if __name__ == '__main__':
    _id = sys.argv[1]
    url_1 = "https://jsonplaceholder.typicode.com/users/{}".format(_id)
    url_2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(_id)
    csv_data = []

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
        csv_data.append([_id,
                         username,
                         task.get('completed'),
                         task.get('title')])

    filename = '{}.csv'.format(_id)

    with open(filename, mode='w') as user_file:
        user_writer = csv.writer(user_file,
                                 delimiter=',',
                                 quotechar='"',
                                 quoting=csv.QUOTE_ALL)

        for task in csv_data:
            user_writer.writerow(task)
