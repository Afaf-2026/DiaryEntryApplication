from pathlib import Path
# Add a new diary entry to the file
def add_entry(filename, date, entry):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{date}: {entry}\n")
# Search for diary entries by date
def search_entries(filename, date):
   # Check if the diary file exists
    if not Path(filename).exists():
        print("Diary file not found.")
        return

    found = False
# Read the file and look for matching dates
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith(f"{date}:"):
                print(line.strip())
                found = True
# Show a message if no matching entry was found
    if not found:
        print("No entries found for this date.")
