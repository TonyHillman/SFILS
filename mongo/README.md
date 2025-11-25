# MISFILS
MISFILS: The MongoDB-based Implementation for the San Francisco Integrated Library System.

This folder contains the submission files for Assignment 2. The remaining folders contain the files from Assignment 1.

Make sure to keep all your Assignment 2 files inside this folder to keep the rest of the folders free from clutter. That way, it will be easier to grade both Assignment 1 and Assignment 2.


# Project Documentation

Here, we maintain the documentation of the project.

This includes how to build and run the software, along with any screenshots that can be of help.

---

# Library Database Application

This project is a Python + MongoDB command-line application for exploring the SFILS (SanFrancisco Integrated Library System). This is a simple application that allows users to view lookup tables to assist with querying patrons by type, home library preference, and notification preference.

## Overview

This application connects to a local MongoDB database name 'SFILS_db'. Users interact with the database using a command-line interface to perform the following functions:

- View lookup tables for patrons, libraries, and notification preferences.
- Search for patrons based on codes outlined in the lookup tables.
- View total patrons registered in system as well as totals by library.
- View activity records for unique patrons

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
|    ---import_data.py
|    ---mongo_CLI.py
|    ---mongo_queries.py
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

- MongoDB 8.2 installed locally
- Python 3.12+ installed
- Required Python packages for the CLI app:

    pip install prettytable pymongo pandas

2. Clone the Repository 

    git clone https://github.com/TonyHillman/SFILS.git
    cd SFILS

3. Create and Load Database

Make sure working directory is set to SFILS

cd yourpath/SFILS

Now run the following:

python mongo/import_data.py

4. Run the application

Make sure working directory is set to SFILS

cd yourpath/SFILS

Now run the following:

python mongo/mongo_CLI.py

The CLI will appear. You can interact with the application by entering keys 1 - 10. 

Keys 1-3 allow users to view lookup tables.
Keys 4-6 allow users to view patrons using codes listed in lookup tables
Keys 7-8 allow users to view total patrons in system and totals by preffered library

Key 9 allows users to exit the interface and close the program

*** NEW Key 10 allows users to view activity records for unique patrons, using _ID field in MongoDB.
Easiest way to use is copy and paste the id when prompted.

5. Additional Notes

The lookup tables from the MySQL version were denormalized into the Patrons collection but CLI functionality 
was preserved. Added a new function in this version of the CLI because I realized my queries were not
using the circulation_activity collection. Otherwise, the CLI app has the same functionality as the MySQL 
version with queries rewritten in MongoDB syntax.

