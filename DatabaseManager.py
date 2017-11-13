import sqlite3

class DatabaseManager(object):
    def __init__(self, db):
        self.conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES)
        self.cur = self.conn.cursor()
        self.create_blogs_table()

    def create_blogs_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS blogs
                    (url text primary key, source text, title text, pub_date timestamp)''')

        self.conn.commit()

    def insert_blog(self, url, source, title, pub_date):
        self.cur.execute('''INSERT INTO blogs VALUES (?, ?, ?, ?)''',(url, source, title, pub_date))

    def __del__(self):
        self.conn.close()
