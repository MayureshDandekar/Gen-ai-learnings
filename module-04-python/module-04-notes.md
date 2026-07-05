# Module 4: Deep Dive in Python — Notes

## Python Inbuilt Libraries

### os
- Interact with OS — paths, folders, env variables
- `os.getcwd()` → current directory
- `os.listdir()` → list files
- `os.getenv("KEY")` → read env variable safely

### csv
- Read/write CSV files
- `csv.reader(file)` → read rows
- `csv.writer(file)` → write rows

### math
- Math beyond +, -, *, /
- `math.sqrt(x)`, `math.ceil(x)`, `math.floor(x)`, `math.pi`

### time
- Delays and measuring execution time
- `time.sleep(seconds)` → pause
- `time.time()` → current timestamp

### datetime
- Dates and times
- `datetime.now()` → current date/time
- `datetime.strftime()` → format date as string

### shutil
- Copy/move/delete files or folders
- `shutil.copy(src, dst)`
- `shutil.move(src, dst)`

### json
- Convert between JSON and Python dict
- File → `json.load()` / `json.dump()`
- String → `json.loads()` / `json.dumps()`

### re (regular expressions)
- Pattern matching, not exact match
- `re.findall(pattern, text)` → all matches
- `re.search(pattern, text)` → first match
- `re.sub(pattern, repl, text)` → find & replace
- Always use raw string `r"..."` for patterns

### random
- Generate random values
- `random.randint(a, b)` → random int in range
- `random.choice(list)` → random item from list
- `random.shuffle(list)` → shuffle list in place