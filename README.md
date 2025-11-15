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
Enter password: hhhh
Score: 35
Rating: Weak
Remarks:
- Good length
- No uppercase letters
- No digits
- No symbols
```

**Moderate Password:**
```
Enter password: 1234
Score: 35
Rating: Weak
Remarks:
- Too short
- No uppercase letters
- No lowercase letters
- No symbols
```

**Strong Password:**
```
Enter password: Qx7lmP@92Lk#VrT8
Score: 80
Rating: Very Strong
Remarks:
- Good length
```

![CI](https://github.com/harshkantvardhan-cloud/password-strength-checker/actions/workflows/ci.yml/badge.svg)
