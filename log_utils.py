import json
from datetime import datetime
import os

import requests 

LOG_FILE = "logs/run_logs.txt"
START_TIME_FILE = "logs/start_time.json"
RESET_FLAG_FILE = "logs/reset_flag.txt"
BEST_RUN_FILE = "logs/best_run.txt"
INITIAL_RUN = True

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def log(message, file=LOG_FILE):
    with open(file, "a") as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")


def get_start_time():
    if os.path.exists(START_TIME_FILE):
        with open(START_TIME_FILE, "r") as f:
            data = json.load(f)
            return data.get("start_time", None)
    return None


def set_start_time(start_time):
    with open(START_TIME_FILE, "w") as f:
        json.dump({"start_time": start_time}, f)


def clear_start_time():
    if os.path.exists(START_TIME_FILE):
        os.remove(START_TIME_FILE)


def get_best_run():
    if os.path.exists(BEST_RUN_FILE):
        with open(BEST_RUN_FILE, "r") as f:
            try:
                return float(f.read())
            except ValueError:
                return None
    return None


def set_best_run(elapsed_time):
    with open(BEST_RUN_FILE, "w") as f:
        f.write(f"{elapsed_time:.2f}")

def send_slack_message(message):
    if SLACK_WEBHOOK_URL:
        payload = {"text": message}
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        if response.status_code == 200:
            print("Slack message sent successfully.")
        else:
            print(f"Failed to send Slack message: {response.status_code}")
    else:
        print("Slack webhook URL not set. Message not sent.")