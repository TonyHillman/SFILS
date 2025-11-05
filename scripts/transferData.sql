# Create indexes to speed up join
CREATE INDEX idx_tempdata_circ
ON temp_data (
    patron_type_code,
    age_range,
    home_library_code,
    notice_preference_code,
    email_provided,
    within_sf_county,
    year_registered
);

CREATE INDEX idx_patron_circ
ON PATRON (
    patron_type_code,
    age_range,
    home_library_code,
    notice_preference_code,
    email_provided,
    within_sf_county,
    year_registered
);

# Run this all together
START TRANSACTION;

# Insert lookup tables first
INSERT INTO PATRON_TYPE (patron_type_code, patron_type_definition)
SELECT DISTINCT patron_type_code, patron_type_definition
FROM temp_data
WHERE patron_type_code IS NOT NULL;

INSERT INTO HOME_LIBRARY (library_code, library_name)
SELECT DISTINCT home_library_code, home_library_name
FROM temp_data
WHERE home_library_code IS NOT NULL;

INSERT INTO NOTICE_PREFERENCE (notice_preference_code, notice_definition)
SELECT DISTINCT notice_preference_code, notice_definition
FROM temp_data
WHERE notice_preference_code IS NOT NULL;

# Now insert into main data tables
INSERT INTO PATRON (
    patron_type_code,
    age_range,
    home_library_code,
    notice_preference_code,
    email_provided,
    year_registered,
    within_sf_county
)
SELECT DISTINCT
    patron_type_code,
    age_range,
    home_library_code,
    notice_preference_code,
    email_provided,
    year_registered,
    within_sf_county
FROM temp_data;

# Join to match parton_id with each record
INSERT INTO CIRCULATION_ACTIVITY (
    total_checkouts,
    total_renewals,
    active_month,
    active_year,
    patron_id
)
SELECT
    t.total_checkouts,
    t.total_renewals,
    t.circulation_active_month,
    t.circulation_active_year,
    p.patron_id
FROM temp_data t
JOIN PATRON p
  ON t.patron_type_code = p.patron_type_code
  AND t.age_range = p.age_range
  AND t.home_library_code = p.home_library_code
  AND t.notice_preference_code = p.notice_preference_code
  AND t.email_provided = p.email_provided
  AND t.within_sf_county = p.within_sf_county
  AND t.year_registered = p.year_registered;

SELECT COUNT(*) AS patron_types FROM PATRON_TYPE;
SELECT COUNT(*) AS libraries FROM HOME_LIBRARY;
SELECT COUNT(*) AS notice_prefs FROM NOTICE_PREFERENCE;
SELECT COUNT(*) AS patrons FROM PATRON;
SELECT COUNT(*) AS circulation_records FROM CIRCULATION_ACTIVITY;

COMMIT;