import json
from pathlib import Path


ROOT = Path(__file__).parents[2]


def load_json(filename: str):
    with (ROOT / "src" / "Data" / filename).open(encoding="utf-8") as file:
        return json.load(file)


def load_portfolio_data() -> tuple[list[dict], dict]:
    return load_json("Projects.json"), load_json("Skills.json")