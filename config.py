from utils.debug import DEBUG, log

COLORS = {
    "bg": "#f6fff6",
    "bg_accent": "#e3f8e5",
    "panel-strong": "#ffffff",
    "text": "#17311f",
    "muted": "#5d7363",
    "primary": "#5bbf5b",
    "primary-strong": "#3ea63e",
    "primary-soft": "#dbf5dd",
}


def getDebugColor():
    if not DEBUG:
        return "#ff000000"

    import random

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"
