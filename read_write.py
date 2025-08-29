"""
read_write.py
Reads a text file and writes a modified version to a new file.
Default transform: add line numbers like "1: ...".

Usage:
    python src/read_write.py
    python src/read_write.py --in input.txt --out output.txt
"""

import argparse
from typing import Iterable

def transform_line(idx: int, line: str) -> str:
    """
    Modify a single line. Current behavior: prefix with line number.
    Keeping trailing newline behavior consistent.
    """
    # We keep the original newline, so don't strip it.
    # Add the number before the line, but avoid adding an extra newline.
    if line.endswith("\n"):
        return f"{idx}: " + line
    else:
        return f"{idx}: {line}\n"

def transform_lines(lines: Iterable[str]) -> Iterable[str]:
    for i, line in enumerate(lines, start=1):
        yield transform_line(i, line)

def main():
    parser = argparse.ArgumentParser(description="Read a file and write a modified version to a new file.")
    parser.add_argument("--in", dest="infile", default="sample_input.txt", help="Path to input text file")
    parser.add_argument("--out", dest="outfile", default="output.txt", help="Path to output text file")
    args = parser.parse_args()

    try:
        with open(args.infile, "r", encoding="utf-8") as f_in:
            with open(args.outfile, "w", encoding="utf-8") as f_out:
                for line in transform_lines(f_in):
                    f_out.write(line)
        print(f"Done. Wrote modified content to: {args.outfile}")
    except FileNotFoundError:
        print(f"Error: Input file not found: {args.infile}")
    except PermissionError:
        print("Error: Permission denied while reading or writing files.")
    except IsADirectoryError:
        print("Error: You provided a directory path instead of a file path.")
    except UnicodeDecodeError:
        print("Error: Could not decode the input file. Make sure it is a UTF-8 text file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()