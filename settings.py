import json
import gameVariables

settings_file = "settings.json"
screenSizes = {"small": [625, 400], "medium": [938, 600], "large": [1250, 800]}


diffs = {"easy": {"projectile": [14, 25], "clip": [50, 100], "damage": [5, 10]},
         "medium": {"projectile": [20, 15], "clip": [20, 150], "damage": [4, 20]},
         "hard": {"projectile": [30, 45], "clip": [12, 220], "damage": [5, 10]}}


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
    gameVariables.bullet_speed = diffs[data["difficulty"]]["projectile"][0]
    gameVariables.rocket_speed = diffs[data["difficulty"]]["projectile"][1]
    gameVariables.clip_size = diffs[data["difficulty"]]["clip"][0]
    gameVariables.reload_speed = diffs[data["difficulty"]]["clip"][1]
    gameVariables.bullet_damage = diffs[data["difficulty"]]["damage"][0]
    gameVariables.rocket_damage = diffs[data["difficulty"]]["damage"][1]
