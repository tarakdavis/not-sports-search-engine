import psycopg2
import csv

conn = psycopg2.connect("dbname=homework user=taradavis")

cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS homework (
        id serial PRIMARY KEY,
        Artist_Name varchar(5),
        Song_Title varchar(60),
        Song_Duration varchar(5),
        Album_Name varchar(60),
        Album_Year integer
        );
    """
)

# Artist Name, Song Title, Song Duration, Album Name, Album Year
with open("drake.csv", 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        # print(row)
        cur.execute(("INSERT INTO homework (Artist_Name, Song_Title, Song_Duration, Album_Name, Album_Year) VALUES (%s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4]))
        conn.commit()


cur.close()
conn.close()
