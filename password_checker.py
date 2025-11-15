import re
from pathlib import Path

def load_common_words(path="common_words.txt"):
    p = Path(path)
    if not p.exists():
        return set()
    return {line.strip().lower() for line in p.read_text(encoding="utf-8").splitlines() if line.strip()}

COMMON_WORDS = load_common_words()

SYMBOLS_REGEX = re.compile(r"[^\w\s]", re.UNICODE)

def score_password(password: str) -> dict:
    score = 0
    remarks = []

    length = len(password)
    if length >= 12:
        score += 25
        remarks.append("Good length")
    elif length >= 8:
        score += 10
        remarks.append("Moderate length")
    else:
        remarks.append("Too short")

    if re.search(r"[A-Z]", password):
        score += 15
    else:
        remarks.append("No uppercase letters")

    if re.search(r"[a-z]", password):
        score += 10
    else:
        remarks.append("No lowercase letters")

    if re.search(r"[0-9]", password):
        score += 15
    else:
        remarks.append("No digits")

    if SYMBOLS_REGEX.search(password):
        score += 15
    else:
        remarks.append("No symbols")

    lower = password.lower()
    for word in COMMON_WORDS:
        if word and word in lower:
            score -= 30
            remarks.append(f"Contains common word: {word}")
            break

    score = max(0, min(100, score))

    if score >= 80:
        rating = "Very Strong"
    elif score >= 60:
        rating = "Strong"
    elif score >= 40:
        rating = "Moderate"
    else:
        rating = "Weak"

    return {"score": score, "rating": rating, "remarks": remarks}

def main():
    pwd = input("Enter password: ")
    res = score_password(pwd)
    print("Score:", res["score"])
    print("Rating:", res["rating"])
    print("Remarks:")
    for r in res["remarks"]:
        print("-", r)

if __name__ == "__main__":
    main()
