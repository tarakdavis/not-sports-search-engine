import psycopg2

conn = psycopg2.connect("dbname=homework user=taradavis")
cur = conn.cursor()


def search():
    x = input("Enter partial or all of a song title to search: ")
    cur.execute("SELECT * FROM homework where song_title ILIKE %(song_title)s", {'song_title': "%" + x.replace(' ', "%") + "%"})
    print(cur.fetchone())
    conn.commit()

def update():
    display()
    u = input("But I guess things change, enter the row's ID#: ")
    # cur.execute("SELECT from homework WHERE id=%s;", (u))
    x = input("Provide a new song title: ")
    cur.execute("UPDATE homework set song_title=%s WHERE id=%s", (x, u))
    conn.commit()
    get_initial_user_input()


def add():
    artist_name = input("First Name Greatest: ")
    song_title = input("One Dance To: ")
    duration = input("From Time: ")
    album_name = input("Drop the mix tape that sh!t sounded like which album: ")
    album_year = int(input("I'm not even Christian I still went to church what year(YYYY): "))
    cur.execute("INSERT INTO homework (Artist_Name, Song_Title, Song_Duration, Album_Name, Album_Year)VALUES(%s, %s, %s, %s, %s)", (artist_name, song_title, duration, album_name, album_year))
    conn.commit()

def display():
    cur.execute("SELECT * FROM homework;")
    results = cur.fetchall()
    print(*results, sep = '\n')


def delete():
    display()
    x = input("Select the corresponding ID# of the row you wish to delete: ")
    cur.execute("DELETE FROM homework WHERE id = %s", (x))
    conn.commit()
    get_initial_user_input()


def get_initial_user_input():
    while True:
        choice = int(input(
            """Enter
[1] to search
[2] to update a row
[3] to add a row
[4] to display the table
[5] to delete
[6] to exit
"""))
        if choice == 1:
            search()
        elif choice == 2:
            update()
        elif choice == 3:
            add()
        elif choice == 4:
            display()
        elif choice == 5:
            delete()
        else:
            print("Hate to see you leave, love to watch you go!")
            break


def main():
    print("Welcome to my realest year!")
    get_initial_user_input()
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
