import os
from dotenv import load_dotenv
import requests

load_dotenv()
AIO_KEY = os.environ.get("AIO_KEY")
FULLNESS_URL = os.environ.get("FULLNESS_URL")
TEMP_URL = os.environ.get("TEMP_URL")

class Fullness:
    def __init__(self, labels, values):
        self.labels = labels
        self.values = values


def get_fullness():
    headers = {"X-AIO-KEY": AIO_KEY}
    fullness_json = requests.get(FULLNESS_URL, headers=headers).json()

    fullness_labels = []
    fullness_values = []

    for data in fullness_json:
        # print(data)
        fullness_labels.append(data["created_at"])
        fullness_values.append(int(data["value"]))

    fullness_data = Fullness(fullness_labels, fullness_values)

    return fullness_data


class Temperature:
    def __init__(self, labels, values):
        self.labels = labels
        self.values = values


def get_temp():
    headers = {"X-AIO-KEY": AIO_KEY}
    temp_json = requests.get(TEMP_URL, headers=headers).json()

    temp_labels = []
    temp_values = []

    for data in temp_json:
        # print(data)
        temp_labels.append(data["created_at"])
        temp_values.append(int(data["value"]))

    temp_data = Temperature(temp_labels, temp_values)

    return temp_data
