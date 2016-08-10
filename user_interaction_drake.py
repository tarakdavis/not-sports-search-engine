import psycopg2

conn = psycopg2.connect("dbname=homework user=taradavis")
cur = conn.cursor()


def search():
    pass
    # ['value'] = psycopg2.Binary('%'+ match_string +'%')
    # cursor.execute("SELECT * FROM some_table WHERE description ILIKE %(value)s;", value)
    # where Name ILIKE %(name)s", {'name': "%" + value.replace(' ', "%") + "%"})



def update():
    #u = input("But I guess things change, enter the row's ID#: ")
    #cur.execute("UPDATE homework set %s=%s WHERE id = %s;", (u))
    pass

def add():
    artist_name = input("First Name Greatest: ")
    song_title = input("One Dance To: ")
    duration = input("From Time: ")
    album_name = input("Drop the mix tape that shit sounded like which album: ")
    album_year = input("I'm not even Christian I still went to church what year(YYYY): ")
    cur.execute("INSERT INTO homework (
                                        """
                                        Artist Name,
                                        Song Title,
                                        Song Duration,
                                        Album Name,
                                        Album Year)
                                        VALUES(%s, %s, %s, %s, %s)",
                                        (artist_name,
                                        song_title,
                                        duration,
                                        album_name,
                                        album_year)
                                        """
                                        )


def display():
    cur.execute("SELECT * FROM homework;")
    results = cur.fetchall()
    print(results)


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
    print("Welcome to my realest year.")
    get_initial_user_input()
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
