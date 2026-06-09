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
    current_data = read()
    new_data = current_data.append(data)
    with open(filename, "a") as file:
        json.dump(new_data, file, indent=4)
