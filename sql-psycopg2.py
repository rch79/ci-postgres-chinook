import psycopg2

# connect to chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object (aka a set, a list, an array) of the database
cursor = connection.cursor()

# Query 1 - select all records from the 'Artist' Table. Queries must always be wrapped in single quotes
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the 'Name' column from the 'Artist' Table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only 'Queen' from the 'Artist' Table:
# cursor.execute ('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only from ArtistId #51 from the 'Artist' table
# cursor.execute ('SELECT * FROM "Artist" WHERE "ArtistId" = 51')

# Query 5 - select only the album with "ArtistId" #51 from the 'Album' table:
cursor.execute ('SELECT * FROM "Album" WHERE "ArtistId" = 51')

#Query 6 - select all tracks from the 'Track' table where composer is "Queen"
cursor.execute ('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection (so it is not always persistent)
connection.close()

# print the results
for result in results:
    print(result)