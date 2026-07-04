# Module 4: Deep Dive in Python — Notes

## Important Built-in Libraries

### `math`
Standard library for math operations beyond basic arithmetic.
```python
import math
print(math.sqrt(16))  # 4.0
```
Use when: square roots, trig, logs, constants (`math.pi`) — anything basic operators can't do.

### `random`
Generates randomness — numbers, choices, shuffles.
```python
import random
print(random.randint(1, 10))          # random int, inclusive both ends
print(random.choice(['apple', 'banana', 'cherry']))  # random pick from a list
```
Use when: simulations, sampling, randomized test data, games.

### `csv`
Reads/writes CSV (comma-separated) files without manually splitting strings on commas.
```python
import csv

with open("example.txt", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])

with open("example.txt", mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```
Key details:
- `mode="w"` = write (overwrites file); `mode="r"` = read.
- `newline=''` on write — prevents extra blank lines between rows on Windows; harmless but correct to always include.
- `csv.writer`/`csv.reader` wrap the file object — you still need `open()` first.
- Reading gives you each row as a **list of strings** (`['Alice', '30', 'New York']`) — note `30` comes back as a string, not an int, since CSV is plain text.

### `os`
Lets Python talk to the operating system — file paths, directories, environment variables — instead of hardcoding OS-specific behavior.
```python
import os

os.getcwd()                  # current working directory
os.listdir('.')              # list files/folders in a directory
os.path.exists('file.txt')   # check if a file/folder exists
os.path.join('folder', 'file.txt')  # build a path safely across OS (Windows vs Mac/Linux use different slashes)
os.makedirs('new_folder', exist_ok=True)  # create a folder (won't error if it already exists)
os.remove('file.txt')        # delete a file
```
Why it matters going forward: this is the exact mechanism your Jarvis project and any future file-based project (loading a PDF for RAG, checking if a `.env` exists, writing logs) relies on. Trigger: any time your code needs to check, create, move, or find something on disk — `os` is the tool.

## Modules & Packages
- **Module** = a single `.py` file you can `import`.
- **Package** = a folder of modules, made importable by adding an `__init__.py` file inside it (as done in `package_folder/`).
- `import mymodule` pulls in a whole file; `from mymodule import myfunction` pulls in just one piece.

## Exception Handling
```python
try:
    risky_code()
except SomeError as e:
    handle_it(e)
finally:
    always_runs()
```
Use when: code might fail (file missing, bad user input, network call) and you want the program to fail gracefully instead of crashing.