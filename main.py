# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from models import Artist, Album, Base, Users, Songs, Favourite  # Import your models from model.py

# engine = create_engine("sqlite:///main.db", echo=True)
# Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# # Create artists, albums, users, and songs here

# art = Artist(artist_name="Migos", genre="Hip Hop")
# art2 = Artist(artist_name="Lil Wayne", genre="Hip Hop")
# art3 = Artist(artist_name="Demathew", genre="Mugithi")
# art4 = Artist(artist_name="Samidoh", genre="Mugithi")

# session.add(art)
# session.add(art2)
# session.add(art3)
# session.add(art4)
# session.commit()

# albm = Album(title="Culture", release="12-03-2014")
# session.add(albm)
# session.commit()

# usr = Users(user_name="alex gikungu", user_email="alexigikungu.012@gmail.com")
# usr2 = Users(user_name="patty muteve", user_email="patty@gmail.com")
# usr3 = Users(user_name="john wick", user_email="wick@gmail.com")
# usr4 = Users(user_name="nany wany", user_email="nany@gmail.com")

# session.add(usr)
# session.add(usr2)
# session.add(usr3)
# session.add(usr4)
# session.commit()

# # Create songs and associate them with artists
# sng = Songs(song_title="pure water", song_duration="3.40", artist=art, genre=art.genre)  # Specify the artist object
# sng2 = Songs(song_title="love wins", song_duration="2.90", artist=art2, genre=art2.genre)  # Specify the artist object
# sng3 = Songs(song_title="jamba ya ruriri", song_duration="3.00", artist=art3, genre=art3.genre)  # Specify the artist object
# sng4 = Songs(song_title="Thie Ukimaga", song_duration="4.12", artist=art4, genre=art4.genre)  # Specify the artist object

# session.add(sng)
# session.add(sng2)
# session.add(sng3)
# session.add(sng4)
# session.commit()

# # Create favorites for the user
# fvs = Favourite(users=usr, songs=sng)  # Specify the user and the songs
# session.add(fvs)
# session.commit()
