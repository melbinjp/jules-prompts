"""What the app does the first time it starts."""
import pathlib
import tomllib

CONFIG = pathlib.Path.home() / ".tidewise" / "config.toml"


def start():
    settings = tomllib.loads(CONFIG.read_text())
    home_beach = settings["home_beach"]
    return plan_screen(home_beach)


def plan_screen(beach):
    return {"screen": "plan", "beach": beach}
