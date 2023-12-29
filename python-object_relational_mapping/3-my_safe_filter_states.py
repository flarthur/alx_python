import MySQLdb as DB
import sys


def states_list(username, password, db_name, new_safe_state):
    try:
        dabase = DB.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
        )

        cur = dabase.cursor()

        list = (
            "SELECT * FROM states WHERE name = %s "
            "OR name LIKE %s COLLATE utf8mb4_bin"
            )

        cur.execute(list, (new_safe_state, new_safe_state + 'N%'))

        states = cur.fetchall()

        for state in states:
            print(state)

    except DB.Error as err:
        print("Error: ", err)
    finally:
        cur.close()
        dabase.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    new_safe_state = sys.argv[4]
    states_list(username, password, db_name, new_safe_state)
