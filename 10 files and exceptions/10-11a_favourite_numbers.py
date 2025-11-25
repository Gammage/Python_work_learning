from pathlib import Path
import json

path = Path("./10 files and exceptions/favourite_numbers_exercise.json")
contents = path.read_text()
print(f"i know your favouriter number, its {contents}")

