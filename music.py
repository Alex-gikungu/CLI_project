# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker,aliased
# from models import Artist, Album, Users, Songs, Favourite
# from sqlalchemy import select
# # Create a SQLAlchemy engine and session
# engine = create_engine("sqlite:///main.db", echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()

# # Function to create the 'reports' directory if it doesn't exist
# def create_reports_directory():
#     os.makedirs('reports', exist_ok=True)

# # Function to create a user account
# def create_account():
#     print("Create Account:")
#     name = input("Name: ")
#     email = input("email: ")
#     password = input("Password: ")
#     confirm_password = input("Confirm Password: ")

#     # Check if passwords match
#     if password != confirm_password:
#         print("Passwords do not match. Account creation failed.")
#     else:
#         # Create a new User and add it to the database
#         user = Users(user_name=name, user_email=email, user_password=password)
#         session.add(user)
#         session.commit()
#         print("Account created successfully!")

# # Function to log in
# def login():
#     print("Login:")
#     email = input("email: ")
#     password = input("Password: ")

#     # Check user credentials and log in
#     user = session.query(Users).filter_by(user_email=email, user_password=password).first()
#     if user:
#         print("Login successful!")
#         main_menu(user)  # After login, display the main menu
#     else:
#         print("Login failed. Please check your credentials.")

# def main_menu(user):
#     while True:
#         print("\nMain Menu:")
#         print("1. Songs")
#         print("2. Albums")
#         print("3. Artists")
#         print("4. Favorite Songs")
#         print("5. Search for Songs")
#         print("6. Exit")

#         choice = input("Select an option: ")

#         if choice == "1":
#             print("You selected 'Songs'.")
#             songs_menu(user)  # Redirect to the Songs menu
#         elif choice == "2":
#             print("You selected 'Albums'.")
#             # Implement functionality to interact with Albums table
#         elif choice == "3":
#             print("You selected 'Artists'.")
#             # Implement functionality to interact with Artists table
#         elif choice == "4":
#             print("You selected 'Favorite Songs'.")
#             favorite_songs_menu(user)  # Redirect to the Favorite Songs menu
#         elif choice == "5":
#             search_songs()  # Implement functionality to search for songs
#         elif choice == "6":
#             print("Exiting the application. Goodbye!")
#             break
#         else:
#             print("Invalid option. Please choose a valid option.")

# def search_songs():
#     search_letter = input("Enter the first letter of the song title: ")
    
#     # Retrieve songs with titles starting with the specified letter
#     songs = session.query(Songs).filter(Songs.song_title.startswith(search_letter)).all()

#     if not songs:
#         print(f"No songs found starting with '{search_letter}'.")
#     else:
#         print(f"Songs starting with '{search_letter}':")
#         for song in songs:
#             print(f"{song.song_title} by {song.album.artist.artist_name}")
# def songs_menu(user):
#     while True:
#         print("\nSongs Menu:")
#         print("1. List Songs")
#         print("2. Add Song")
#         print("3. Delete Song")  # Add an option for deleting songs
#         print("4. Back to Main Menu")
#         option = input("Select an option: ")

#         if option == "1":
#             list_songs()
#         elif option == "2":
#             add_song(user)
#         elif option == "3":
#             delete_song()  # Call the delete_song function
#         elif option == "4":
#             return
#         else:
#             print("Invalid option. Please choose a valid option.")


# def list_songs():
#     # Query songs and their associated artist names
#     songs = session.query(Songs.song_title, Songs.song_duration, Songs.genre, Artist.artist_name). \
#         join(Artist).all()

#     print("\nList of Songs:")
#     for song in songs:
#         print(f"Song Title: {song.song_title}")
#         print(f"Artist: {song.artist_name}")
#         print(f"Song Duration: {song.song_duration}")
#         print(f"Genre: {song.genre}\n")

#     input("Press Enter to continue...")

# def add_song(user):
#     print("Add a Song:")
#     title = input("Song Title: ")
#     duration = input("Song Duration: ")
#     artist_name = input("Artist Name: ")
#     genre=input("Genre: ")

#     # Check if the artist exists, or create a new artist if not
#     artist = session.query(Artist).filter_by(artist_name=artist_name).first()
#     if not artist:
#         artist = Artist(artist_name=artist_name, genre=genre)  # Add default genre here
#         session.add(artist)
#         session.commit()

#     # Create a new song and add it to the database
#     song = Songs(song_title = title, song_duration = duration,artist=artist,genre= genre)
#     session.add(song)
#     session.commit()

#     print("Song added successfully!")

# def delete_song():
#     song_title = input("Enter the title of the song you want to delete: ")

#     # Query the song to be deleted
#     song_to_delete = session.query(Songs).filter_by(song_title = song_title).first()

#     if song_to_delete:
#         print(f"Deleting the song: {song_to_delete.song_title}")
        
#         # Delete the song from the session
#         session.delete(song_to_delete)
#         session.commit()

#         print("Song deleted successfully!")
#     else:
#         print(f"Song with title '{song_title}' not found.")

#     input("Press Enter to continue...")

# def favorite_songs_menu(user):
#     while True:
#         print("\nFavorite Songs Menu:")
#         print("1. List Favorite Songs")
#         print("2. Add Favorite Song")
#         print("3. Remove from Favorite")
#         print("4. Back to Main Menu")

#         choice = input("Select an option: ")

#         if choice == "1":
#             list_favorite_songs(user)  # Implement functionality to list favorite songs
#         elif choice == "2":
#             add_favorite_song(user)  # Implement functionality to add a favorite song
#         elif choice == "3":
#             remove_from_favorite()  # Call the remove_from_favorite function
#         elif choice == "4":
#             break  # Return to the Main Menu
#         else:
#             print("Invalid option. Please choose a valid option.")

# def list_favorite_songs(user):
#     # Implement functionality to list favorite songs
#     favorite_songs = session.query(Favourite).filter_by(users=user).all()
#     if not favorite_songs:
#         print("No favorite songs found.")
#     else:
#         print("List of Favorite Songs:")
#         for index, favorite in enumerate(favorite_songs, start=1):
#             print(f"{index}. {favorite.songs.song_title} by {favorite.songs.artist.artist_name}")

# # Rest of your code...


# def add_favorite_song(user):
#     print("Add a Favorite Song:")
#     song_title = input("Song Title: ")
#     artist_name = input("Artist Name: ")

#     # Check if the song and artist exist in the database, and add them to the user's favorites
#     song = session.query(Songs).\
#         join(Artist, Songs.artist_id == Artist.artist_id).\
#         filter(Songs.song_title == song_title, Artist.artist_name == artist_name).first()

#     if not song:
#         print("Song or artist not found.")
#         return

#     # Correct the argument name from 'user' to 'users'
#     favorite = Favourite(users=user, songs=song)
#     session.add(favorite)
#     session.commit()

#     print("Favorite song added successfully!")


# def remove_from_favorite():

#     song_title = input("Enter the song title to remove from the favorite list: ")

#     # Query the userfavorite table to find the song by title
#     song_to_remove = session.query(Favourite).join(Songs).filter(Songs.song_title == song_title).first()

#     if song_to_remove:
#         print(f"Deleting the song: {song_to_remove.songs.song_title}")
        
#         # Delete the song from the session
#         session.delete(song_to_remove)
#         session.commit()

#         print("Song deleted successfully!")
#     else:
#         print(f"Song with title '{song_title}' not found in favorites.")

#     input("Press Enter to continue...")

# # Make sure you import the necessary models:

# if __name__ == '__main__':
#     create_reports_directory()

#     while True:
#         print("\nOptions:")
#         print("1. Create Account")
#         print("2. Login")
#         print("3. Exit")

#         option = input("Select an option: ")

#         if option == "1":
#             create_account()
#         elif option == "2":
#             login()
#         elif option == "3":
#             print("Exiting the application. Goodbye!")
#             break
#         else:
#             print("Invalid option. Please choose a valid option.")
