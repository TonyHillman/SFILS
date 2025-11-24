import pandas as pd
from pymongo import MongoClient
import math

# Deals with empty columns, stores data as int or NULL
def safe_int(val):
    return int(val) if pd.notna(val) and not math.isnan(val) else None

# Connect to MongoDB and read Csv
client = MongoClient("mongodb://localhost:27017/")
db = client.SFILS_db
patrons_collection = db.patrons
activity_collection = db.circulation_activity

df = pd.read_csv(
    r"C:\Users\tonyh\Documents\GitHub\SFILS\app\SFPL_DataSF_library-usage_Jan_2023_CLEAN.csv"
)

# Use these columns to define unique patrons
patron_columns = [
    "patron_type_code",
    "age_range",
    "home_library_code",
    "notice_preference_code",
    "email_provided",
    "within_sf_county",
    "year_registered"
]

# Define unique patrons
unique_patrons = df.drop_duplicates(subset=patron_columns).reset_index(drop=True)

# Insert unique patrons and build mapping 
# Key of columns maps to _id in Mongo
patron_mapping = {}

for index, row in unique_patrons.iterrows():
    doc = {
        "patron_type": {
            "code": row["patron_type_code"],
            "definition": row["patron_type_definition"]
        },
        "home_library": {
            "code": row["home_library_code"],
            "name": row["home_library_name"]
        },
        "notice_preference": {
            "code": row["notice_preference_code"],
            "definition": row["notice_definition"]
        },
        "age_range": row["age_range"],
        "email_provided": bool(row["email_provided"]),
        "within_sf_county": bool(row["within_sf_county"]),
        "year_registered": safe_int(row["year_registered"]) # safe_int function handles NULLS
    }

    result = patrons_collection.insert_one(doc)
    key = tuple(row[col] for col in patron_columns)
    patron_mapping[key] = result.inserted_id

# Insert circulation activity
for index, row in df.iterrows():
    key = tuple(row[col] for col in patron_columns)
    patron_id = patron_mapping[key]

    activity_doc = {
        "patron_ref": patron_id,
        "total_checkouts": safe_int(row["total_checkouts"]),
        "total_renewals": safe_int(row["total_renewals"]),
        "active_month": (row["circulation_active_month"]),
        "active_year": safe_int(row["circulation_active_year"])
    }

    activity_collection.insert_one(activity_doc)

print("Import done")
