"""
Main module for DB Mentorship program.

DO NOT UPDATE THIS FILE.
"""

import argparse
import os
import sys

from bson import json_util
import requests
from dotenv import load_dotenv

from tasks import task_3

load_dotenv()

# DO NOT UPDATE THIS OBJECT
TASK_MAP = {
    3: task_3,
}


URL = os.environ["API_URL"]


# DO NOT UPDATE THIS CODE
def parse_arguments():
    parser = argparse.ArgumentParser(description="DB Mentorship Query Checker")

    parser.add_argument(
        "-t",
        "--task_num",
        type=int,
        help="Task number to check (check discord for the task number). For ex. 3",
        required=True,
    )
    parser.add_argument(
        "-e",
        "--email",
        type=str,
        help="Your registered email id",
        required=True,
    )

    return parser.parse_args()


# DO NOT UPDATE THIS CODE
def send_query_for_evaluation(query, task_num, question_name, email):

    serialised_query = json_util.dumps(query)
    body = {
        "taskId": str(task_num),
        "questionId": question_name,
        "query": serialised_query,
        "email": email,
    }
    print(body)

    response = requests.put(
        URL,
        json=body,
        timeout=30,
    )

    if int(response.status_code / 100) != 2:
        print(response.text)
        print(
            f"Failed to send result for evaluation. Status code: {response.status_code}."
            + "Please contact on discord."
        )
        sys.exit(1)

    data = response.json()
    print(data)


# DO NOT UPDATE THIS CODE
def main(task_num, email):
    if task_num not in TASK_MAP:
        print(f"Task {task_num} not found")
        sys.exit(1)

    task = TASK_MAP[task_num]

    for question in task.QUESTIONS_LIST:
        query = question()
        send_query_for_evaluation(query, task_num, question.__name__, email)


# DO NOT UPDATE THIS CODE
if __name__ == "__main__":
    args = parse_arguments()

    main(args.task_num, args.email)
