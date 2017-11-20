from os import path, getcwd
import sqlite3
from datetime import datetime, timedelta

class DatabaseManager(object):
    def __init__(self, db_name):
        project_path = path.dirname(getcwd())
        db_dir = 'database'
        db_path = path.join(project_path, db_dir, db_name)
        self.con = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
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

    def delete_old_blogs(self):
        with self.con:
            self.cur.execute('select * from blogs')
            for row in self.cur.fetchall():
                url = row[0]
                pub_date = row[3]
                timezone = pub_date.tzinfo
                now_in_timezone = datetime.now(timezone)
                one_year_ago = now_in_timezone - timedelta(days=365)
                if pub_date < one_year_ago:
                    self.cur.execute('delete from blogs where url=?', url)

    def get_all_blogs(self):
        with self.con:
            self.cur.execute('select * from blogs')
            return self.cur.fetchall()

    def __del__(self):
        self.con.close()
