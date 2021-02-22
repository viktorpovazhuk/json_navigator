import copy
from pprint import pprint
from typing import List, Dict, Union

import requests


def show_object(json_obj: Union[List, Dict]):
    print("Enter key 'e' to exit an application.")

    cur_obj = copy.deepcopy(json_obj)

    pprint(cur_obj)
    key = ''
    while True:
        if isinstance(cur_obj, list):
            print('Choose index (0,1,...) of item from the list')
            pprint(cur_obj)
        elif isinstance(cur_obj, dict):
            print('Choose from object keys')
            print(f"keys: {', '.join(cur_obj.keys())}")
        else:
            print('You get to value')
            print(f'{key}: {cur_obj}')
            while True:
                print('Start from the beginning (y/n)?')
                answer = input()
                if answer == 'y' or answer == 'n':
                    break
                else:
                    print("Incorrect answer. Type 'y' or 'n'")
            if answer == 'y':
                cur_obj = copy.deepcopy(json_obj)
                continue
            else:
                break

        key = input()
        if isinstance(cur_obj, list):
            key = int(key)

        if key == 'e':
            break

        try:
            cur_obj = cur_obj[key]
        except Exception as exc:
            print('Enter another key: ' + str(exc))


def get_object():
    url = "https://api.twitter.com/2/users/by"
    token = 'AAAAAAAAAAAAAAAAAAAAAG7KMwEAAAAA54JdYkWN17qlqjSHWfSGzR' \
            'wxzaY%3DDZte5Xdq1mXJkHOsAWyXSBcMiDssP5q8hUZvve7evDXHOIDmFa'
    headers = {'Authorization': 'Bearer ' + token}
    params = {
        'usernames': 'Valsorya2Go,elonmusk',
        'user.fields': 'location,created_at'
    }

    resp = requests.get(url, headers=headers, params=params)

    return resp.json()


def navigate_object():
    json_obj = get_object()

    show_object(json_obj)


if __name__ == '__main__':
    navigate_object()
