USE library_db;

CREATE TABLE temp_data (
    patron_type_code TINYINT,
    patron_type_definition VARCHAR(50),
    total_checkouts INT,
    total_renewals INT,
    age_range VARCHAR(25),
    home_library_code CHAR(5),
    home_library_name VARCHAR(50),
    circulation_active_month CHAR(9),
    circulation_active_year YEAR,
    notice_preference_code CHAR(5),
    notice_definition CHAR(10),
    email_provided BOOLEAN,
    within_sf_county BOOLEAN,
    year_registered YEAR
);

SET GLOBAL local_infile = 1;