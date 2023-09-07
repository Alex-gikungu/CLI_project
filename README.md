# Music Library Project

## Author
Alex Gikungu

## Description
The Music Library Project is a Python application for managing music-related data using SQLAlchemy. It allows you to create and manage artists, albums, users, songs, and user favorite lists. This project is designed to help you organize your music collection, add new songs, and keep track of your favorite tracks.

## How It Works
The project is structured around five main classes: `Artist`, `Album`, `Users`, `Songs`, and `Favorite`, which are managed using SQLAlchemy. Here's how the project works:

- **Database Setup**: The project uses an SQLite database to store music-related data. SQLAlchemy is used to define and create the database schema.

- **Data Relationships**: The classes establish relationships between artists, albums, users, songs, and user favorites. For example, songs are associated with artists and albums, and users can create lists of favorite songs.

- **Data Management**: The application provides methods to interact with these classes, such as adding new artists, albums, users, songs, and favorite songs. It also allows you to query the database for information.

- **User Interaction**: The `main.py` file serves as the entry point for the application. Users can run this file to interact with the project. The application prompts users with options to perform various tasks, and user input is processed to execute the desired operations.

- **Testing**: The project includes a `seeds.py` file that can be used to populate the database with sample data for testing and initial setup.

## Getting Started

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone git@github.com:Alex-gikungu/CLI_project.git

2. Navigate to the repository's directory:
   
    cd CLI_project

3. Install project dependencies using Pipenv:

   pipenv install

4. Activate the virtual environment:
   
   pipenv shell

### How to run the project 

To interact with the project and see how it works run the following command in the terminal 

  python3 music.py 

##  License 

This project is licensed under the [MIT License](LICENSE).