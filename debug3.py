import sys
import traceback

try:
    exec(open('password_checker.py').read())
except Exception as e:
    traceback.print_exc()
