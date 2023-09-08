from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from models import Artist, Album, Base, Users, Songs, Favourite

# Create SQLAlchemy engine and session
engine = create_engine("sqlite:///main.db", echo=True)
Base.metadata.create_all(bind=engine) 
Session = sessionmaker(bind=engine)
session = Session()

# Creating artist objects
art = Artist(artist_name="Migos", genre="Hip Hop")
art2 = Artist(artist_name="Lil Wayne", genre="Hip Hop") 
art3 = Artist(artist_name="Demathew", genre="Mugithi")
art4 = Artist(artist_name="Samidoh", genre="Mugithi")

# Add artists to session
session.add(art)
session.add(art2) 
session.add(art3)
session.add(art4)

# Commit artist changes
session.commit() 

# # Create album object
# albm = Album(title="Culture", release="12-03-2014")

# # Add and commit album 
# session.add(albm)
# session.commit()

# # Create user objects
# usr = Users(user_name="alex gikungu", user_email="alexigikungu.012@gmail.com", user_password=1234)

# # Add and commit users
# session.add(usr) 
# session.commit()

# # Create song objects associated with artists
# sng = Songs(song_title="pure water", song_duration="3.40", artist=art, genre=art.genre)

# # Add and commit songs
# session.add(sng)   
# session.commit()

# # Create favorite association for user
# fvs = Favourite(users=usr, songs=sng) 

# # Add and commit favorite
# session.add(fvs)
# session.commit()