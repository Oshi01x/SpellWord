import json
import random
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def load_words():
    """JSON файлынан сөздерді қателерді өңдей отырып жүктеу."""
    try:
        with open("words.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            # Егер файл бос болса, резервті сөз қайтару
            if not data or not any(data.values()):
                return {"easy": ["python"]}
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        # Файл табылмаса немесе зақымдалса, осы сөзді қайтару
        return {"easy": ["flask"]}


@app.route("/")
def index():
    """Ойынның басты беті."""
    return render_template("index.html")


@app.route("/get_word")
def get_word():
    """Араластырылған кездейсоқ сөзді қайтаратын эндпоинт."""
    data = load_words()

    # Барлық деңгейдегі сөздерді бір тізімге жинау
    all_words = []
    for level in data.values():
        if isinstance(level, list):  # Мәннің тізім екенін тексеру
            all_words.extend(level)

    if not all_words:
        all_words = ["flask", "python"]

    # Кездейсоқ сөз таңдап, оны кіші әріпке келтіру
    original = random.choice(all_words).strip().lower()

    # Әріптерді міндетті түрде өзгеретіндей етіп араластыру
    scrambled_list = list(original)
    if len(original) > 1:
        attempts = 0
        # Сөз бастапқы қалпынан өзгергенше (макс. 10 рет) араластыру
        while "".join(scrambled_list) == original and attempts < 10:
            random.shuffle(scrambled_list)
            attempts += 1

    # Нәтижені JSON форматында фронтендке жіберу
    return jsonify(
        {
            "scrambled": "".join(scrambled_list).upper(),
            "original": original,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
