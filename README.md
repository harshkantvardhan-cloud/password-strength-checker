# Password Strength Checker

Small Python utility to evaluate password strength. Features:

- Command-line password scoring via `password_checker.py`.
- Simple GUI interface in `gui_password_checker.py`.
- Unit tests under `tests/` using `pytest`.

To run tests:

```
python -m pytest -v
```

This repository includes a small list of common words used to penalize weak passwords.

## Examples

Here are example password evaluations:

**Weak Password:**
```
Enter password: password123
Score: 35
Rating: Weak
Remarks:
- No uppercase letters
- Contains common word: password
```

**Moderate Password:**
```
Enter password: MyPassword2024
Score: 60
Rating: Strong
Remarks:
- Good length
```

**Strong Password:**
```
Enter password: Tr0pic@lThunder2024!
Score: 100
Rating: Very Strong
Remarks:
- Good length
```

![CI](https://github.com/harshkantvardhan-cloud/password-strength-checker/actions/workflows/ci.yml/badge.svg)
