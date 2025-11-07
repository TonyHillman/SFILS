
from prettytable import PrettyTable

# Show patron lookup table
def show_patron_types(cursor):
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
def show_notice_pref(cursor):
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
def show_library_pref(cursor):
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

# Show Patrons by Type
def lookup_patrons_by_type(cursor):
    code = input("\nEnter valid patron type code: ").strip()
    
    cursor.execute("""
        SELECT patron_id, patron_type_code, age_range, home_library_code
        FROM PATRON
        WHERE patron_type_code = %s
        ORDER BY patron_id
    """, (code,))
    
    rows = cursor.fetchall()
    if rows:
        table = PrettyTable(["ID", "Type", "Age Range", "Library"])
        for row in rows:
            table.add_row(row)
        print(f"\nPatrons with type {code}")
        print(table)
    else:
        print(f"No patrons found for type {code}.")

# Show Patrons by Notification Preference
def lookup_patrons_by_notice_pref(cursor):
    code = input("\nEnter valid Notification Preference code: ").strip()
    
    cursor.execute("""
        SELECT patron_id, patron_type_code, age_range, home_library_code, notice_preference_code
        FROM PATRON
        WHERE notice_preference_code = %s
        ORDER BY patron_id
    """, (code,))
    
    rows = cursor.fetchall()
    if rows:
        table = PrettyTable(["ID", "Type", "Age Range", "Library", "Notice Pref"])
        for row in rows:
            table.add_row(row)
        print(f"\nPatrons with notification preference {code}")
        print(table)
    else:
        print(f"No patrons found for notification preference {code}.")

# Show Patrons by Home Library
def lookup_patrons_by_library_code(cursor):
    code = input("\nEnter valid Home Library code: ").strip()
    
    cursor.execute("""
        SELECT patron_id, patron_type_code, age_range, home_library_code
        FROM PATRON
        WHERE home_library_code = %s
        ORDER BY patron_id
    """, (code,))
    
    rows = cursor.fetchall()
    if rows:
        table = PrettyTable(["ID", "Type", "Age Range", "Library"])
        for row in rows:
            table.add_row(row)
        print(f"\nPatrons in library {code}")
        print(table)
    else:
        print(f"No patrons found for library {code}.")

# Show number of Patrons for each Library
def total_by_library(cursor):
    cursor.execute("""
        SELECT h.library_name, COUNT(p.patron_id)
        FROM PATRON p
        JOIN HOME_LIBRARY h ON p.home_library_code = h.library_code
        GROUP BY h.library_name
        ORDER BY h.library_name
    """)
    rows = cursor.fetchall()
    table = PrettyTable(["Library", "Number of Patrons"])
    for row in rows:
        table.add_row(row)
    print("\nPatron counts by library")
    print(table)

# Show number of Patrons in DB
def total_patrons(cursor):
    cursor.execute("SELECT COUNT(*) FROM PATRON")
    count = cursor.fetchone()[0]
    print(f"\nTotal Patrons: {count}")