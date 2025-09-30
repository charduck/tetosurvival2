# ----------- LOADING SETTINGS FUNCTIONS ----------- #
try:
    import json
except ImportError:
    print("ImportError caught in loadsettings.")

def loadSettings():
    try:
        with open("data/settings.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"music": True, "resolution": [1280, 720]} # default values
    
def saveSettings(settings):
    with open("data/settings.json", "w") as f:
        json.dump(settings, f)
