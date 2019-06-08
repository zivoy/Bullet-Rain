import json
import gameVariables
import stage

settings_file = "settings.json"
screenSizes = {"small": (625, 400), "medium": (938, 600), "large": (1250, 800)}

diffs = {"easy": {"projectile": [12, 7], "clip": [30, 40], "damage": [4, 10], "bullet rain": 35},
         "medium": {"projectile": [15, 10], "clip": [12, 80], "damage": [5, 15], "bullet rain": 50},
         "hard": {"projectile": [20, 15], "clip": [5, 150], "damage": [7, 20], "bullet rain": 70}}

stage_choice = ''


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
    gameVariables.rain_amount = diffs[data["difficulty"]]["bullet rain"]
    gameVariables.stage_choice = 1
    gameVariables.img = "opt4.jpg"
    gameVariables.bull_size = gameVariables.screenSize[1] * 0.001625
    gameVariables.roke_size = gameVariables.screenSize[1] * 0.00625
    #stage.createStage(gameVariables.stage_choice)
