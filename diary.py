from pathlib import Path


def add_entry(filename, date, entry):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{date}: {entry}\n")


def search_entries(filename, date):
    if not Path(filename).exists():
        print("Diary file not found.")
        return

    found = False

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith(f"{date}:"):
                print(line.strip())
                found = True

    if not found:
        print("No entries found for this date.")