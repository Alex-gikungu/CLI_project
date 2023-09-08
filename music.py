# Importing libraries
import os
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from models import Artist, Album, Users, Songs, Favourite 

# Creating SQLAlchemy database engine and session
engine = create_engine("sqlite:///main.db", echo=True)  
Session = sessionmaker(bind=engine)
session = Session()

# Function to create reports directory
def create_reports_directory():
  os.makedirs('reports', exist_ok=True) 

# Function to create a new user account  
def create_account():
  
  # Get user input
  name = input("Name: ")
  email = input("Email: ")
  password = input("Password: ")
  confirm_password = input("Confirm Password: ")

  # Validate password match
  if password != confirm_password:
    print("Passwords do not match. Account creation failed.")
  else:   
    # Creating and adding User object
    user = Users(user_name=name, user_email=email, user_password=password)
    session.add(user)
    session.commit()
    print("Account created successfully!")

# Function for user to login
def login():

  # Get login credentials
  email = input("Email: ")
  password = input("Password: ")

  # Query for user
  user = session.query(Users).filter_by(user_email=email, user_password=password).first()
  
  # Check if user found and login
  if user:
    print("Login successful!")
    main_menu(user)  
  else:
    print("Login failed. Please check your credentials.")

# Main menu function 
def main_menu(user):

  # Menu loop
  while True:
    # Print options
    print("\nMain Menu:")
    print("1. Songs")
    print("2. Albums")
    print("3. Artists")
    print("4. Favorite Songs")
    print("5. Search for Songs")
    print("6. Exit")

    choice = input("Select an option: ")
    
    # Call appropriate function based on choice
    if choice == "1":
      songs_menu(user)  
    elif choice == "2":
      print("You selected 'Albums'.")        
    elif choice == "3":
      print("You selected 'Artists'.")         
    elif choice == "4":
      favorite_songs_menu(user)   
    elif choice == "5":
      search_songs()
    elif choice == "6":
      print("Exiting the application. Goodbye!")
      break
    else:
      print("Invalid option. Please choose a valid option.")

# Allow searching songs by first letter 
def search_songs():
  
  search_letter = input("Enter the first letter of the song title: ")
  # Query for songs with title starting with search letter
  songs = session.query(Songs).filter(Songs.song_title.startswith(search_letter)).all()

  if not songs:
    print(f"No songs found starting with '{search_letter}'.")
  else:
    print(f"Songs starting with '{search_letter}':")
    # Print matching songs
    for song in songs:
      print(f"Song Title: {song.song_title}")
      print(f"Artist: {song.artist_id}")
      print("")

  input("Press Enter to continue to the main menu.")

# Menu for song CRUD operations
def songs_menu(user):
  
  while True:

    print("\nSongs Menu:")
    print("1. List Songs")
    print("2. Add Song")
    print("3. Delete Song")
    print("4. Back to Main Menu")
    
    option = input("Select an option: ")

    if option == "1":
      list_songs()
    elif option == "2":
      add_song(user)
    elif option == "3":
      delete_song()
    elif option == "4":
      return
    else:
      print("Invalid option. Please choose a valid option.")

# Print list of all songs
def list_songs():
  # Query for song data 
  songs = session.query(Songs.song_title, Songs.song_duration, Songs.genre, Artist.artist_name).\
    join(Artist).all()

  print("\nList of Songs:")
  
  # Print songs
  for song in songs:
    print(f"Song Title: {song.song_title}")
    print(f"Artist: {song.artist_name}")
    print(f"Song Duration: {song.song_duration}")
    print(f"Genre: {song.genre}\n")

  input("Press Enter to continue...")

# Add a new song
def add_song(user):
  
  # Get song details
  title = input("Song Title: ")
  duration = input("Song Duration: ")
  artist_name = input("Artist Name: ")
  genre = input("Genre: ")

  # Get or create artist
  artist = session.query(Artist).filter_by(artist_name=artist_name).first()
  if not artist:
    artist = Artist(artist_name=artist_name, genre=genre)
    session.add(artist)
    session.commit()

  # Creating and add song
  song = Songs(song_title=title, song_duration=duration, artist=artist, genre=genre)
  session.add(song)
  session.commit()

  print("Song added successfully!")
  
# Delete a song  
def delete_song():

  song_title = input("Enter the title of the song you want to delete: ")

  # Query for song
  song_to_delete = session.query(Songs).filter_by(song_title=song_title).first()

  # Delete song if found
  if song_to_delete:
    print(f"Deleting the song: {song_to_delete.song_title}")      
    session.delete(song_to_delete)
    session.commit()
    print("Song deleted successfully!")
  else:
    print(f"Song with title '{song_title}' not found.")

  input("Press Enter to continue...")

# Menu for managing user's favorite songs
def favorite_songs_menu(user):

  while True:
    print("\nFavorite Songs Menu:")

    print("1. List Favorite Songs")
    print("2. Add Favorite Song")
    print("3. Remove from Favorite")
    print("4. Back to Main Menu")

    choice = input("Select an option: ")

    if choice == "1":
      list_favorite_songs(user)
    elif choice == "2":
      add_favorite_song(user)
    elif choice == "3":
      remove_from_favorite()
    elif choice == "4":
      break
    else:
      print("Invalid option. Please choose a valid option.")

# Print user's favorited songs 
def list_favorite_songs(user):
  favorite_songs = session.query(Favourite).filter_by(users=user).all()

  if not favorite_songs:
    print("No favorite songs found.")
  else:
    print("List of Favorite Songs:")
    for index, favorite in enumerate(favorite_songs, start=1):
      print(f"{index}. {favorite.songs.song_title} by {favorite.songs.artist.artist_name}")

# Add song to user's favorites
def add_favorite_song(user):
  
  print("Add a Favorite Song:")
  song_title = input("Song Title: ")
  artist_name = input("Artist Name: ")

  # Query for song
  song = session.query(Songs).\
    join(Artist, Songs.artist_id == Artist.artist_id).\
    filter(Songs.song_title == song_title, Artist.artist_name == artist_name).first()

  if not song:
    print("Song or artist not found.")
    return
  
  # Creating and add favorite association
  favorite = Favourite(users=user, songs=song)
  session.add(favorite)
  session.commit()

  print("Favorite song added successfully!")

# Remove song from user's favorites
def remove_from_favorite():
  song_title = input("Enter the song title to remove from the favorite list: ")

  # Query for favorited song
  song_to_remove = session.query(Favourite).join(Songs).filter(Songs.song_title == song_title).first()

  if song_to_remove:
    print(f"Deleting the song: {song_to_remove.songs.song_title}")  
    session.delete(song_to_remove)
    session.commit()
    print("Song deleted successfully!")
  else:
    print(f"Song with title '{song_title}' not found in favorites.")

  input("Press Enter to continue...")

# Main script  
if __name__ == '__main__':

  create_reports_directory()

  while True:
    print("\nOptions:")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    option = input("Select an option: ")

    if option == "1":
      create_account()
    elif option == "2":
      login()
    elif option == "3":
      print("Exiting the application. Goodbye!")
      break
    else:
      print("Invalid option. Please choose a valid option.")