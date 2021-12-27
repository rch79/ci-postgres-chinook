from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the chinook database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for
# a session to create a new instance of sessionmaker, then point to
# our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# Query 1 - Select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(f"{artist.ArtistId} | {artist.Name}")

# Query 2 - Select only the Name column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - Select only "Queen" from the "Artist" table
# .first() method below will only return the firts result from the 
# filter_by method
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(f"{artist.ArtistId} | {artist.Name}")

# Query 4 - Select only by "ArtistId" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(f"{artist.ArtistId} | {artist.Name}")

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(f"{album.AlbumId} | {album.Title} | {album.ArtistId}")


# Query 6 - select only the tracks with "Composer" "Queen" on the "Track" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(f"{track.TrackId} | {track.Name} | {track.Composer}")
