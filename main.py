from diary import add_entry, search_entries


#This function runs the diary menu
def main():
    filename = input("Enter diary file name: ")
    # Keep showing the menu until the user exits
    while True:
        print("\nDiary Application")
        print("1. Add a diary entry")
        print("2. Search by date")
        print("3. Change diary file")
        print("4. Exit")

        choice = input("Choose an option: ")
       # Add new diary entry
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            entry = input("Write your diary entry: ")
            add_entry(filename, date, entry)
            print("Entry saved!")
       # Search for diary entries by date
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            search_entries(filename, date)
        # Change to another diary file
        elif choice == "3":
            filename = input("Enter another diary file name: ")
        # Exit the diary application
        elif choice == "4":
            print("Goodbye!")
            break
        # Show a message if the user enters a wrong option
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
