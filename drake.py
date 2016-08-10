import psycopg2
import csv

conn = psycopg2.connect("dbname=homework user=taradavis")

cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS homework (
        id serial PRIMARY KEY,
        Artist Name varchar(10),
        Song Title varchar(50),
        Song Duration varchar(5),
        Album Name varchar(50),
        Album Year date,
        );
    """
)

# Artist Name, Song Title, Song Duration, Album Name, Album Year
with open('drake.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        cur.execute("INSERT INTO homework (Artist Name, Song Title, Song Duration, Album Name, Album Year) VALUES(%s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5]))
    conn.commit()
    cur.close()

conn.close()
