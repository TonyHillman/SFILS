

from pymongo import MongoClient
from mongo_queries import (
    show_patron_types, show_library_pref, show_notice_pref,
    lookup_patrons_by_type, lookup_patrons_by_library_code,
    lookup_patrons_by_notice_pref, total_by_library, total_patrons,
    lookup_patron_activity
)

client = MongoClient("mongodb://localhost:27017/")
db = client.SFILS_db
patrons_collection = db.patrons
activity_collection = db.circulation_activity

def main():
    choice = 0
    while choice != "9":
        print("\n\tLibrary Interface (MongoDB Version)")
        print("\n1. Show Patron Lookup Table")
        print("2. Show Notification Preferences Lookup Table")
        print("3. Show Home Library Lookup Table")
        print("4. Lookup Patrons by Type Code")
        print("5. Lookup Patrons by Notification Preference Code")
        print("6. Lookup Patrons by Home Library Code")
        print("7. Total Patrons by Library")
        print("8. Total Patrons in System")
        print("9. Exit Program")
        print("10. Lookup activity for patron")
        choice = input("\nSelect option 1 - 10: ").strip()

        if choice == "1":
            show_patron_types(patrons_collection)
        elif choice == "2":
            show_notice_pref(patrons_collection)
        elif choice == "3":
            show_library_pref(patrons_collection)
        elif choice == "4":
            lookup_patrons_by_type(patrons_collection)
        elif choice == "5":
            lookup_patrons_by_notice_pref(patrons_collection)
        elif choice == "6":
            lookup_patrons_by_library_code(patrons_collection)
        elif choice == "7":
            total_by_library(patrons_collection)
        elif choice == "8":
            total_patrons(patrons_collection)
        elif choice == "9":
            print("Closing program\n")
            break
        elif choice == "10":
            lookup_patron_activity(patrons_collection, activity_collection)
        else:
            print("Invalid Choice, Please enter number 1 - 10")

if __name__ == "__main__":
    main()
