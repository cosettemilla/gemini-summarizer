from pathlib import Path

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def write_text(path: Path, text: str):
    path.write_text(text, encoding="utf-8")
