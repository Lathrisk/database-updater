# database-updater
Iterate through some databases and apply some SQL

## Instructions
Run the script with python providing the following arguments:

`python update.py -c [pathtoconnectionfile] -s [pathtosqlfile]`

Where the connection file is an `.ini` file with a list of database connections in the format shown in the `databases.ini` file.
And the SQL file is the SQL you want to apply to each database in turn.
