from password_checker import score_password

def test_empty():
    r = score_password("")
    assert r["rating"] in ["Weak", "Moderate", "Strong", "Very Strong"]

def test_common_word():
    r = score_password("Password123!")
    assert any("common" in remark.lower() for remark in r["remarks"])

def test_strong_password():
    r = score_password("Ex@mpleStrong2025!!")
    assert r["rating"] in ["Strong", "Very Strong"]
