from password_checker import score_password


def validate_result(res):
    assert isinstance(res, dict)
    assert 0 <= res.get("score", -1) <= 100
    assert res.get("rating") in ["Weak", "Moderate", "Strong", "Very Strong"]
    assert isinstance(res.get("remarks"), list)


def test_unicode_password():
    r = score_password("Pässw0rd!😊")
    validate_result(r)


def test_very_long_password():
    pwd = "A1!" * 50  # long mixed password
    r = score_password(pwd)
    validate_result(r)
    assert r["rating"] in ["Strong", "Very Strong"]


def test_only_symbols():
    r = score_password("!@#$%^&*()_+-=[]{};:'\"|,./<>?")
    validate_result(r)


def test_repeated_characters():
    r = score_password("aaaaaaAAAAAA111111!!!!!!")
    validate_result(r)
    assert r["score"] >= 40
