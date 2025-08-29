"""
error_handling.py
Ask the user for a filename, attempt to read it, and handle common errors.
Enter 'q' to quit.
"""

def try_read_file(path: str) -> bool:
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        print("\n=== File content preview (first 200 chars) ===")
        print(content[:200])
        print("\nRead succeeded. File length:", len(content), "characters.")
        return True
    except FileNotFoundError:
        print("Error: File not found. Please check the name and try again.")
    except PermissionError:
        print("Error: Permission denied. You might not have rights to read this file.")
    except IsADirectoryError:
        print("Error: That path is a directory, not a file.")
    except UnicodeDecodeError:
        print("Error: Could not decode this file as UTF-8 text.")
    except Exception as e:
        print("Unexpected error:", e)
    return False

def main():
    print("Enter a filename to read (or 'q' to quit).")
    while True:
        path = input("Filename: ").strip()
        if path.lower() == 'q':
            print("Goodbye.")
            break
        if path == "":
            print("Please enter a non-empty filename.")
            continue
        if try_read_file(path):
            break  # Stop after a successful read

if __name__ == "__main__":
    main()