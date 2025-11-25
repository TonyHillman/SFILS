
from prettytable import PrettyTable
from bson import ObjectId

def show_patron_types(patrons_collection):
    pipeline = [
        {"$group": 
            {
                "_id": "$patron_type.code",
                "definition": {"$first": "$patron_type.definition"}
            }
        },
        {"$sort": {"_id": 1}}
    ]
    
    rows = list(patrons_collection.aggregate(pipeline))
    
    if rows:
        table = PrettyTable(["Code", "Description"])
        for r in rows:
            table.add_row([r["_id"], r["definition"]])
        print("\nPatron Types")
        print(table)
    else:
        print("No patron types found.")



def show_notice_pref(patrons_collection):
    pipeline = [
        {"$group": 
            {
                "_id": "$notice_preference.code",
                "definition": {"$first": "$notice_preference.definition"}
            }
        },
        {"$sort": {"_id": 1}}
    ]
    
    rows = list(patrons_collection.aggregate(pipeline))
    
    if rows:
        table = PrettyTable(["Code", "Description"])
        for r in rows:
            table.add_row([r["_id"], r["definition"]])
        print("\nNotification Preferences")
        print(table)
    else:
        print("No Notification Preferences found.")



def show_library_pref(patrons_collection):
    pipeline = [
        {"$group": 
            {
                "_id": "$home_library.code",
                "name": {"$first": "$home_library.name"}
            }
        },
        {"$sort": {"_id": 1}}
    ]
    
    rows = list(patrons_collection.aggregate(pipeline))
    
    if rows:
        table = PrettyTable(["Code", "Name"])
        for r in rows:
            table.add_row([r["_id"], r["name"]])
        print("\nLibraries")
        print(table)
    else:
        print("No Libraries found.")



def lookup_patrons_by_type(patrons_collection):
    code = int(input("\nEnter valid patron type code: ").strip())
    
    rows = list(patrons_collection.find(
        {"patron_type.code": code},
        {"patron_type.code": 1, "age_range": 1, "home_library.code": 1}
    ).sort("_id", 1))
    
    if rows:
        table = PrettyTable(["ID", "Type", "Age Range", "Library"])
        for r in rows:
            table.add_row([str(r["_id"]), code, r["age_range"], r["home_library"]["code"]])
        print(f"\nPatrons with type {code}")
        print(table)
    else:
        print(f"No patrons found for type {code}.")




def lookup_patrons_by_notice_pref(patrons_collection):
    code = input("\nEnter valid Notification Preference code: ").strip()
    
    rows = list(patrons_collection.find(
        {"notice_preference.code": code},
        {"patron_type.code": 1, "age_range": 1,
         "home_library.code": 1, "notice_preference.code": 1}
    ).sort("_id", 1))
    
    if rows:
        table = PrettyTable(["ID", "Type", "Age Range", "Library", "Notice Pref"])
        for r in rows:
            table.add_row([
                str(r["_id"]),
                r["patron_type"]["code"],
                r["age_range"],
                r["home_library"]["code"],
                code
            ])
        print(f"\nPatrons with notification preference {code}")
        print(table)
    else:
        print(f"No patrons found for notification preference {code}.")



def lookup_patrons_by_library_code(patrons_collection):
    code = input("\nEnter valid Home Library code: ").strip()
    
    rows = list(patrons_collection.find(
        {"home_library.code": code},
        {"patron_type.code": 1, "age_range": 1, "home_library.code": 1}
    ).sort("_id", 1))
    
    if rows:
        table = PrettyTable(["ID", "Type", "Age Range", "Library"])
        for r in rows:
            table.add_row([str(r["_id"]), r["patron_type"]["code"], r["age_range"], code])
        print(f"\nPatrons in library {code}")
        print(table)
    else:
        print(f"No patrons found for library {code}.")



def total_by_library(patrons_collection):
    pipeline = [
        {"$group": {
            "_id": "$home_library.name",
            "count": {"$sum": 1}
        }},
        {"$sort": {"_id": 1}}
    ]
    
    rows = list(patrons_collection.aggregate(pipeline))
    
    table = PrettyTable(["Library", "Number of Patrons"])
    for r in rows:
        table.add_row([r["_id"], r["count"]])
    
    print("\nPatron counts by library")
    print(table)



def total_patrons(patrons_collection):
    count = patrons_collection.count_documents({})
    print(f"\nTotal Patrons: {count}")


# New function, allows viewing activity records for each patron
# Copy patron id to use 
def lookup_patron_activity(patrons_collection, activity_collection):
    pid = input("Enter patron ID: ").strip()
    
    try:
        oid = ObjectId(pid)
    except:
        print("Invalid ID")
        return

    patron = patrons_collection.find_one({"_id": oid})
    
    if not patron:
        print("Patron not found.")
        return

    activities = list(activity_collection.find({"patron_ref": oid}).sort([("active_year", 1), ("active_month", 1)]))

    print("\n=== Patron Info ===")
    print(f"Type: {patron['patron_type']['code']} ({patron['patron_type']['definition']})")
    print(f"Age Range: {patron['age_range']}")
    print(f"Home Library: {patron['home_library']['code']} ({patron['home_library']['name']})")
    print(f"Email Provided: {patron['email_provided']}")
    print(f"Within SF County: {patron['within_sf_county']}")
    print(f"Year Registered: {patron['year_registered']}")

    if activities:
        table = PrettyTable(["Month", "Year", "Checkouts", "Renewals"])
        for a in activities:
            table.add_row([
                a["active_month"],
                a["active_year"],
                a["total_checkouts"],
                a["total_renewals"]
            ])
        
        print("\n=== Circulation Activity ===")
        print(table)
    else:
        print("\nNo circulation activity found.")