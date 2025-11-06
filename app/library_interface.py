

import mysql.connector  
from prettytable import PrettyTable

# Create connection
conn = mysql.connector.connect(
    host="localhost",
    user="user_read_only",
    password="uaa1234",
    database="library_db"
)
cursor = conn.cursor()

# Show patron lookup table
def show_patron_types():
    cursor.execute("SELECT patron_type_code, patron_type_definition FROM PATRON_TYPE ORDER BY patron_type_code;")
    rows = cursor.fetchall()
    if rows:
        table = PrettyTable(["Code", "Description"])
        for row in rows:
            table.add_row(row)
        print("\nPatron Types")
        print(table)
    else:
        print("No patron types found.")

# Show Notification Preference lookup table
def show_notice_pref():
    cursor.execute("SELECT notice_preference_code, notice_definition FROM notice_preference ORDER BY notice_preference_code;")
    rows = cursor.fetchall()
    if rows:
        table = PrettyTable(["Code", "Description"])
        for row in rows:
            table.add_row(row)
        print("\nNotification Preferences")
        print(table)
    else:
        print("No Notification Preferences found.")

# Show Home Library lookup table
def show_library_pref():
    cursor.execute("SELECT library_code, library_name FROM home_library ORDER BY library_code;")
    rows = cursor.fetchall()
    if rows:
        table = PrettyTable(["Code", "Name"])
        for row in rows:
            table.add_row(row)
        print("\nLibraries")
        print(table)
    else:
        print("No Libraries found.")

# Display CLI      
def main():
    choice = 0
    while choice != "8":
        print("\n\tLibrary Interface")
        print("\n1. Show Patron Lookup Table")
        print("2. Show Notification Preferences Lookup Table")
        print("3. Show Home Library Lookup Table")
        print("8. Exit Program")
        choice = input("\nSelect option 1 - 8: ").strip()

        if choice == "1":
            show_patron_types()
        elif choice == "2":
            show_notice_pref()
        elif choice == "3":
            show_library_pref()
        elif choice == "8":
            print("Closing program\n")
            break
        else:
            print("Invalid Choice, Please enter number 1 - 8")

           


if __name__ == "__main__":
    main()
    cursor.close()
    conn.close()