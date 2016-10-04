# not-sports-search-engine

- Designed a database structure (schema) to fit data model. 
- The data model is how the statistics are organized.
- Created a python file to insert a sample of data (no more than 20 rows) into the database using the cursor.execute method with some INSERT statements.
- Program connects to the database and asks the user to search by name. For a given result set, the program displays the results in a clean manner to the user.
- Added a feature that allows a user to insert new data into the database. 
- Prompts the user for every column that is needed to provide custom information.

## objectives

- Understand fundamentals of Database Schema design.
- Understand basic SQL syntax to:
  - create tables
  - query for data
  - insert data
- Create helper functions to allow for easier interaction with your database.

## files included
- drake.py - opens the drake.csv and reads it into a python file then adds the data to a database
- drake.csv - contains data related to Drake's top 20 most popular songs (according to a quick google search)
- user_interaction_drake.py - file contains logic for main program
- requirements.txt - in your command line: 'pip install -r requirements.txt' to run on your machine
