from pathlib import Path

BASE_DIR = Path(**file**).parent

def load_file(filename):
path = BASE_DIR / filename
if not path.exists():
return ""
return path.read_text(encoding="utf-8")

poem_rules = load_file("시규칙.txt")
song_rules = load_file("Ai노래연구.txt")
format_rules = load_file("규칙.txt")

print("=== SunoMakerReverse ===")
print("시규칙:", len(poem_rules), "chars")
print("Ai노래연구:", len(song_rules), "chars")
print("규칙:", len(format_rules), "chars")

print("Knowledge Base Loaded Successfully")
