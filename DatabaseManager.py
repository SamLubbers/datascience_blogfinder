import sqlite3

class DatabaseManager(object):
    def __init__(self, db):
        self.con = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES)
        self.cur = self.con.cursor()
        self.create_blogs_table()

    def create_blogs_table(self):
        with self.con:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS blogs
                        (url text primary key, host text, title text, pub_date timestamp)''')

    def insert_blog(self, url, host, title, pub_date):
        try:
            with self.con:
                self.cur.execute('''INSERT INTO blogs VALUES (?, ?, ?, ?)''', (url, host, title, pub_date))
        except sqlite3.IntegrityError:
            pass # avoid the same website from being added twice

    def __del__(self):
        self.con.close()
