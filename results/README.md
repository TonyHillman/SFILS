# Findings

This folder contains our findings from this database project.

The findings include details about the library patrons. For example, how many from the age range 0 to 9 years used the library, how many of them were repeat patrons (can be found from total checkouts), how many renewed (can be found from total renewals).

# Performance Metrics

This folder also contains the performance values.

Did we store the data in our database appropriately?

This is meant to be a more manageable database with multiple tables. We are not simply dumping the whole Excel sheet into one giant MySQL table.

------------------
Found that there were 26822 unique patrons in the system. Located in the screenshots folder 
can see total unique patrons by library. Also performance data for the creation of database and inserts into tables can be found in screenshots. Note that when attempting to reproduce 
my setup, the last insertion into CIRCULATION_ACTIVITY table is not working properly and timing out. When I orignally ran the setup, I think that statement ran in about 7 seconds.