from diary import add_entry, search_entries


def main():
    filename = input("Enter diary file name: ")

    while True:
        print("\nDiary Application")
        print("1. Add a diary entry")
        print("2. Search by date")
        print("3. Change diary file")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            entry = input("Write your diary entry: ")
            add_entry(filename, date, entry)
            print("Entry saved!")

        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            search_entries(filename, date)

        elif choice == "3":
            filename = input("Enter another diary file name: ")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
