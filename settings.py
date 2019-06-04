import json
import gameVariables

settings_file = "settings.json"
screenSizes = {"Small": [625, 400], "Medium": [938, 600], "Large": [1250, 800]}


def write(data):
    with open(settings_file, "w") as settings:
        json.dump(data, settings)


def read():
    with open(settings_file, "r") as settings:
        return json.load(settings)


def compose():
    pass


def load():
    pass