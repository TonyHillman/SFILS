# Project Documentation

Here, we maintain the documentation of the project.

This includes how to build and run the software, along with any screenshots that can be of help.

---

# Library Database Application

This project is a Python + MySQL command-line application for exploring the SFILS (SanFrancisco Integrated Library System). This is a simple application that allows users to view lookup tables to assist with querying patrons by type, home library preference, and notification preference.

## Overview

This application connects to a local MySQL database name 'library_db' using a read-only user. Users interact with the database using a command-line interface to perform the following functions:

- View lookup tables for patrons, libraries, and notification preferences.
- Search for patrons based on codes outlined in the lookup tables.
- View total patrons registered in system as well as totals by library.

## Project Structure

SFILS/
│
├── app/
│   ├── library_interface.py
│   ├── library_queries.py
│   └── README.md
│
├── docs/
│   └── README.md
│
├── mongo/
│   └── README.md
│
├── results/
│   └── README.md
│
├── scripts/
│   ├── createDumpTable.sql
│   ├── createTables.sql
│   ├── createUser.sql
│   ├── loadData.sql
│   ├── transferData.sql
│   └── README.md
│
└── README.md

## Setup Instructions

1. Prerequisites

Ensure you have the following:

- MySQL Server 8.0+ installed locally
- Admin privileges on your MySQL server
- Python 3.12+ installed
- Required Python packages for the CLI app:

    pip install mysql-connector-python prettytable

2. Clone the Repository 

    git clone https://github.com/TonyHillman/SFILS.git
    cd SFILS

3. Create and Load Database

Now run the following scripts located in SFILS/scripts folder in the following order
using a MySQL account with admin privileges:

    1. scripts/createDumpTable.sql            (Creates database and temporary table)
    2. scripts/createTables.sql               (Creates relational tables for DB)
    3. scripts/loadData.sql                   (Loads data into temporary table)
    4. scripts/transferData.sql               (Transfers data into relational tables)
    5. scripts/createUser.sql                 (Create read-only user for CLI application)

4. Configue Python Application

The CLI app is already set to use the read-only user created in script 5. If you wish to
change the user or password then update the connection information in library_interface.py 
located in this section of code:

    # Create connection
    conn = mysql.connector.connect(
        host="localhost",
        user="user_read_only",
        password="uaa1234",
        database="library_db"
    )
    cursor = conn.cursor()

5. Run the application

Make sure working directory is set to SFILS

cd yourpath/SFILS

Now run the following:

python app/library_interface.py

The CLI will appear. You can interact with the application by entering keys 1 - 9. 

Keys 1-3 allow users to view lookup tables.
Keys 4-6 allow users to view patrons using codes listed in lookup tables
Keys 7-8 allow users to view total patrons in system and totals by preffered library

Key 9 allows users to exit the interface and close the program

6. Additional Notes

Ensure scripts are run in the order outlined above.
PrettyTable is used for CLI terminal readability.