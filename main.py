from diary import add_entry, search_entries


def main():
   """
    This function runs the diary application
    It lets the user add entries, search by date, change the diary file, or exit the program
    """
   filename = input("Enter diary file name: ")

   # keep showing the menu  until the user chooses to exit.  
   while True:
        print("\nDiary Application")
        print("1. Add a diary entry")
        print("2. Search by date")
        print("3. Change diary file")
        print("4. Exit")

        choice = input("Choose an option: ")
        # Add a new diary entry
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            entry = input("Write your diary entry: ")
            add_entry(filename, date, entry)
            print("Entry saved!")
   # Search for diary entries by date
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            search_entries(filename, date)
   # Change the diary file
        elif choice == "3":
            filename = input("Enter another diary file name: ")
   # Exit the diary application
        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
