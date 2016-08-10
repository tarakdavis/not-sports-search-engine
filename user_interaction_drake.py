import psycopg2


def search():
    # get_initial_user_input()
    pass


def update():
    #cur.execute("UPDATE homework set #first_name = 'Tara' WHERE id = 2;")
    # get_initial_user_input()
    pass

def add():
    artist_name = input("First Name Greatest: ")
    song_title = input("One Dance To: ")
    duration = input("From Time: ")
    album_name = input("Drop the mix tape that shit sounded like which album: ")
    album_year = input("I'm not even Christian I still went to church what year(YYYY): ")
    cur.execute("INSERT INTO homework (Artist Name, Song Title, Song Duration, \
    Album Name, Album Year) VALUES(%s, %s, %s, %s, %s)", (artist_name,
    song_title, duration, album_name, album_year))
    get_initial_user_input()


def display():
    cur.execute("SELECT * FROM homework;")
    results = cur.fetchall()
    print(results)
    get_initial_user_input()


def delete():
    display()
    x = input("Select the corresponding ID# of the row you wish to delete: ")
    cur.execute("DELETE FROM homework WHERE id = %s)", (x))
    get_initial_user_input()


def get_initial_user_input():
    while True:
        choice = input(
            "Enter [1] to search, [2] to update a row, [3] to add a row, [4] to display the table, [5] to delete, [6] to exit: "
        )
        if choice == '1':
            search()
        elif choice == '2':
            update()
        elif choice == '3':
            add()
        elif choice == '4':
            display()
        elif choice == '5':
            delete()
        elif choice == '6':
            print("If you're reading this, it's too late...")
            break
        else:
            print("I'm just saying that you could do better.")
            break
    conn.commit()


def main():
    conn = psycopg2.connect("dbname=homework user=taradavis")
    cur = conn.cursor()
    print("Welcome to my realest year.")
    get_initial_user_input()
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
