#!/usr/bin/python3

"""
A module in which I would make requests to a fake API.
"""
import requests
import sys


def retrieveInfo(userId):
    "Takes a user id, retrieves it's todo info and return it as json"

    r = requests.get(
        f'https://jsonplaceholder.typicode.com/todos/?userId={userId}')
    return r.json()


def getNumberOfTasksDone(tasks):
    "Takes an array of data, and returns number of tasks done in it"

    numOfTasksDone = 0
    for task in tasks:
        if task["completed"]:
            numOfTasksDone += 1

    return numOfTasksDone


def getEmployeeName(empId):
    "Takes an emp id, and returns it's name"

    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{empId}')
    return r.json()['name']


def getCompletedTasksTitles(tasks):
    "Takes an array of tasks, and returns the titles of all completed tasks"

    titles = []
    for task in tasks:
        if task['completed']:
            titles.append(task['title'])

    return titles


def solution(empId):
    """
    Takes an emp id, retrieves it's data from jsonplaceholder api,
    then print it in a certain format
    """

    name = getEmployeeName(empId)
    tasks = retrieveInfo(empId)
    numOfDoneTasks = getNumberOfTasksDone(tasks)
    totalNumOfTasks = len(tasks)
    titles = getCompletedTasksTitles(tasks)

    message1 = f"Employee {name} is done with tasks"
    message2 = f"({numOfDoneTasks}/{totalNumOfTasks}):"
    print(message1 + message2)
    for title in titles:
        print(f"\t {title}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('Usage: ./file_name employeeId')
        exit(1)

    solution(sys.argv[1])
