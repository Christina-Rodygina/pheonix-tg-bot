import sqlite3


def connected_db():
    db = sqlite3.connect("C:\\Users\\krist\\PycharmProjects\\andrey_tg_bot\\core\\utils\\base1.db")
    c = db.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS users (
        chat_id text,
        key_data text
    )""")

    return db, c


async def registration(chat_id, key_data):
    db, c = connected_db()
    try:
        c.execute(f"INSERT INTO users VALUES ('{chat_id}', '{key_data}')")
        db.commit()
        db.close()
        return True
    except Exception as e:
        print(e)
        db.close()


async def check_registration(chat_id):
    db, c = connected_db()
    try:
        c.execute("SELECT chat_id "
                  "FROM users "
                  "WHERE chat_id = ?", (chat_id,))
        result = c.fetchone()
        if result is not None and result[0] == str(chat_id):
            db.close()
            return True
        else:
            db.close()
            return False
    except Exception as e:
        print(e)
        db.close()


async def check_key(key_data):
    db, c = connected_db()
    try:
        c.execute("""SELECT chat_id
                  FROM users
                  WHERE key_data = ?""", (key_data, ))
        result1 = c.fetchone()
        db.close()
        return result1
    except Exception as e:
        print(e)
        db.close()
