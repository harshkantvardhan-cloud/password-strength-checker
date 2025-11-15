import ast
import sys

# Read the file source
with open('password_checker.py', 'r') as f:
    source = f.read()

# Parse it
tree = ast.parse(source)

# Print all top-level names
print("Top-level definitions in password_checker.py:")
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        print(f"  Function: {node.name}")
    elif isinstance(node, ast.ClassDef):
        print(f"  Class: {node.name}")
    elif isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name):
                print(f"  Variable: {target.id}")

print("\n\nNow trying to import:")
try:
    import password_checker
    print("Import successful")
    print("Module dict keys:", list(password_checker.__dict__.keys()))
except Exception as e:
    print(f"Import failed: {e}")
    import traceback
    traceback.print_exc()
