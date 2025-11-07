

import mysql.connector  
from library_queries import (
    show_patron_types, show_library_pref, show_notice_pref,
    lookup_patrons_by_type, lookup_patrons_by_library_code,
    lookup_patrons_by_notice_pref, total_by_library, total_patrons
)

# Create connection
conn = mysql.connector.connect(
    host="localhost",
    user="user_read_only",
    password="uaa1234",
    database="library_db"
)
cursor = conn.cursor()


# Display CLI      
def main():
    choice = 0
    while choice != "9":
        print("\n\tLibrary Interface")
        print("\n1. Show Patron Lookup Table")
        print("2. Show Notification Preferences Lookup Table")
        print("3. Show Home Library Lookup Table")
        print("4. Lookup Patrons by Type Code")
        print("5. Lookup Patrons by Notification Preference Code")
        print("6. Lookup Patrons by Home Library Code")
        print("7. Total Patrons by Library")
        print("8. Total Patrons in System")
        print("9. Exit Program")
        choice = input("\nSelect option 1 - 9: ").strip()

        if choice == "1":
            show_patron_types(cursor)
        elif choice == "2":
            show_notice_pref(cursor)
        elif choice == "3":
            show_library_pref(cursor)
        elif choice == "4":
            lookup_patrons_by_type(cursor)
        elif choice == "5":
            lookup_patrons_by_notice_pref(cursor)
        elif choice == "6":
            lookup_patrons_by_library_code(cursor)
        elif choice == "7":
            total_by_library(cursor)
        elif choice == "8":
            total_patrons(cursor)
        elif choice == "9":
            print("Closing program\n")
            break
        else:
            print("Invalid Choice, Please enter number 1 - 9")

           
if __name__ == "__main__":
    main()
    cursor.close()
    conn.close()