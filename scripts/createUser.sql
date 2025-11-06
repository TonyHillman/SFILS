
#Create user for application
CREATE USER 'user_read_only'@'localhost' IDENTIFIED BY 'uaa1234';
GRANT SELECT ON library_db.* TO 'user_read_only'@'localhost';
FLUSH PRIVILEGES;