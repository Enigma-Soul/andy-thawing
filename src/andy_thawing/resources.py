import sys
from pathlib import Path


def get_resources_dir() -> Path:
    if getattr(sys, 'frozen', False):
        base = Path(sys._MEIPASS)
    else:
        base = Path(__file__).resolve().parent.parent.parent
    return base / "resources"


def font_path(name: str) -> Path:
    return get_resources_dir() / "fonts" / name


def img_path(name: str) -> Path:
    return get_resources_dir() / "img" / name
