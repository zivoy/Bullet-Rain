import json
import gameVariables

settings_file = "settings.json"
screenSizes = {"small": [625, 400], "medium": [938, 600], "large": [1250, 800]}
diffs = {"easy": [], "medium": [], "hard": []}


def write(data, file=settings_file):
    with open(file, "w") as settings:
        json.dump(data, settings)


def read(file=settings_file):
    with open(file, "r") as settings:
        return json.load(settings)


def compose():
    write(gameVariables.settings)


def load():
    gameVariables.settings = read()


def apply():
    data = gameVariables.settings
    gameVariables.screenSize = screenSizes[data["screen"].lower()]
    gameVariables.player_lives = data["lives"]
    gameVariables.player_health = data["health per life"]
    gameVariables.power_ups = data["power-ups"]
