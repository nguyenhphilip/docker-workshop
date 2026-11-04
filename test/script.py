from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name # script.py

print(f"Files in {current_dir}: {[item.name for item in current_dir.iterdir()]}")

for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue
    else:
        print(f" - {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encoding='utf-8')
        print(f"    Content: {content}")