

CREATE TABLE PATRON_TYPE (
    patron_type_code TINYINT PRIMARY KEY,
    patron_type_definition VARCHAR(50) NOT NULL
);

CREATE TABLE HOME_LIBRARY (
    library_code CHAR(5) PRIMARY KEY,
    library_name VARCHAR(50) NOT NULL
);

CREATE TABLE NOTICE_PREFERENCE (
    notice_preference_code CHAR(5) PRIMARY KEY,
    notice_definition CHAR(10) NOT NULL
);

CREATE TABLE PATRON (
    patron_id INT AUTO_INCREMENT PRIMARY KEY,
    patron_type_code TINYINT,
    age_range VARCHAR(25),
    home_library_code CHAR(5),
    notice_preference_code CHAR(5),
    email_provided BOOLEAN,
    year_registered YEAR,
    within_sf_county BOOLEAN,
    FOREIGN KEY (patron_type_code) REFERENCES PATRON_TYPE(patron_type_code),
    FOREIGN KEY (home_library_code) REFERENCES HOME_LIBRARY(library_code),
    FOREIGN KEY (notice_preference_code) REFERENCES NOTICE_PREFERENCE(notice_preference_code)
);


CREATE TABLE CIRCULATION_ACTIVITY (
    circulation_id INT AUTO_INCREMENT PRIMARY KEY,
    total_checkouts INT,
    total_renewals INT,
    active_month CHAR(9),
    active_year YEAR,
    patron_id INT,
    FOREIGN KEY (patron_id) REFERENCES PATRON(patron_id)
);