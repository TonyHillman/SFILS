

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/SFPL_DataSF_library-usage_Jan_2023_CLEAN.csv'
INTO TABLE temp_data
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
  patron_type_code,
  patron_type_definition,
  total_checkouts,
  total_renewals,
  age_range,
  home_library_code,
  home_library_name,
  circulation_active_month,
  @circulation_active_year,
  notice_preference_code,
  notice_definition,
  @email_provided,
  @within_sf_county,
  year_registered
)
SET
  circulation_active_year = NULLIF(@circulation_active_year, ''),
  email_provided = IF(LOWER(@email_provided) IN ('true', '1'), 1, 0),
  within_sf_county = IF(LOWER(@within_sf_county) IN ('true', '1'), 1, 0);


