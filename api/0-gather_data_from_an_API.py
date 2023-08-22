#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}")
    todo = requests.get(f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos")
    u = user.json()
    t = todo.json()
    tr = []
    for dicc in t:
        for k, v in dicc.items():
            if k == 'completed':
                if v == True:
                    tr.append(dicc)
    print(f"Employee {u.get('name')} is done with tasks({(len(tr))}/{(len(t))}):")
    for tittle in tr:
        for k, v in tittle.items():
            if k == 'title':
                print(f'	 {v}')
