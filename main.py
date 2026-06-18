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

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/rules")
def rules():
    return {"rules": RULES[:3000]}

@app.get("/lyrics")
def lyrics():
    return {"lyrics": LYRICS[:3000]}


@app.get("/genre")
def genre(keyword: str = ""):
    if not keyword:
        return {"message": "Please provide a keyword"}

    results = []

    for line in GENRES.splitlines():
        if keyword.lower() in line.lower():
            results.append(line)

    return {
        "keyword": keyword,
        "results": results[:30]
    }

