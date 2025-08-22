import sqlite3, time

def db_poll_loop(db_file, callback):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    while True:
        cur.execute("SELECT * FROM messages WHERE processed=0")
        rows = cur.fetchall()
        for row in rows:
            callback(row[1])
            cur.execute("UPDATE messages SET processed=1 WHERE id=?", (row[0],))
        conn.commit()
        time.sleep(2)
