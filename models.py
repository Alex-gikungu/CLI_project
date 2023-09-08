from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
#artist table
class Artist(Base):
    __tablename__ = "artist"

    artist_id = Column(Integer, primary_key=True)
    artist_name = Column(String)
    genre = Column(String)

    # Define a relationship to the Songs model
    songs = relationship("Songs", back_populates="artist")


#album table 
class Album(Base):
    __tablename__ = "album"

    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    release = Column(String)

#user table
class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_email = Column(String)
    user_password = Column(String)

    # Define a relationship to the Favourite model
    userfavorite = relationship("Favourite", back_populates="users")

#songs table
class Songs(Base):
    __tablename__ = "songs"

    song_id = Column(Integer, primary_key=True)
    song_title = Column(String)
    song_duration = Column(String)
    artist_id = Column(Integer, ForeignKey("artist.artist_id"))  # Define the foreign key
    genre = Column(String)

    # Define relationships to the Artist and Favourite models
    artist = relationship("Artist", back_populates="songs")
    userfavorite = relationship("Favourite", back_populates="songs")

#userfavorite table 
class Favourite(Base):
    __tablename__ ="userfavorite"

    userfavourite_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))  # Define the foreign key
    song_id = Column(Integer, ForeignKey("songs.song_id"))    # Define the foreign key

    # Define relationships to the Users and Songs models
    users = relationship("Users", back_populates="userfavorite")
    songs = relationship("Songs", back_populates="userfavorite")
