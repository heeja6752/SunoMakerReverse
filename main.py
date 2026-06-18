from pathlib import Path

BASE_DIR = Path(__file__).parent

def load_file(filename):
    path = BASE_DIR / filename

    if not path.exists():
        return ""

    return path.read_text(encoding="utf-8")

RULES = load_file("규칙.txt")
GENRES = load_file("Ai노래연구.txt")
LYRICS = load_file("가사목록.txt")

print("SunoMakerReverse Started")
print("Rules:", len(RULES))
print("Genres:", len(GENRES))
print("Lyrics:", len(LYRICS))
