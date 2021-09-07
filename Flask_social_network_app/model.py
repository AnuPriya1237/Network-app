import sqlite3
import os
script_path = os.path.dirname(os.path.relpath(__file__))
print(__file__)

def create_post(name, content):
    connection = sqlite3.connect(os.path.join(script_path,'database.db'))
    cur = connection.cursor()
    cur.execute('insert into posts(name,content) values (?,?)',(name, content))

    connection.commit()
    connection.close()



def get_posts():
    connection = sqlite3.connect(os.path.join(script_path, 'database.db'))
    cur = connection.cursor()
    cur.execute('select * from posts')
    post = cur.fetchall()
    return post



