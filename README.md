# File Handling & Exception Handling Assignment

This repo contains two small Python programs for your assignment.

## What to submit
Push **all files** from this folder to your GitHub repository:

```
.
├── README.md
├── .gitignore
├── requirements.txt
├── sample_input.txt
└── src
    ├── read_write.py
    └── error_handling.py
```

> Do not rename the files. Keep the structure as shown.

## How to run

Use Python 3.9+.

### 1) File Read & Write Challenge
Reads a file and writes a **modified** version to a new file by adding line numbers.

```bash
# default: reads sample_input.txt and writes to output.txt
python src/read_write.py

# or specify files
python src/read_write.py --in sample_input.txt --out my_output.txt
```

**Expected output** (first lines of `output.txt`):
```
1: Hello, World!
2: This is a sample file.
3: Each line will be prefixed with its line number.
```

### 2) Error Handling Lab
Asks the user for a filename, tries to read it, and handles errors if it does not exist or cannot be read.

```bash
python src/error_handling.py
```

Try the following inputs when prompted:
- A valid file like `sample_input.txt`
- A missing file like `missing.txt`
- A directory like `src`

## Notes
- The code is beginner friendly and well commented.
- No third-party packages are required.
- If you want to change the transform logic, edit `transform_line()` in `src/read_write.py`.
- `error_handling.py` keeps prompting until you enter a readable file or `q` to quit.

## Suggested commit steps

```bash
git init
git add .
git commit -m "Add file and exception handling assignment"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

Good luck!