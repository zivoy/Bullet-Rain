import json
import gameVariables

settings_file = "settings.json"
screenSizes = {"small": [625, 400], "medium": [938, 600], "large": [1250, 800]}


def write(data):
    with open(settings_file, "w") as settings:
        json.dump(data, settings)


def read():
    with open(settings_file, "r") as settings:
        return json.load(settings)


def compose():
    pass


def load():
    data = read()
    gameVariables.screenSize = screenSizes[data["screen"].lower()]
    gameVariables.player_lives = data["lives"]
    gameVariables.player_health = data["health per life"]
