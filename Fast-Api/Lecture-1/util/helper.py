from config import filename
import json


def read():
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def write(data: dict):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
