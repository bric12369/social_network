from lib.post import *

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            post = Post(row['id'], row['title'], row['content'], row['views'], row['user_id'])
            posts.append(post)
        return posts
    
    def find(self, post_id):
        rows = self._connection.execute('SELECT * FROM posts WHERE id = %s', [post_id])
        row = rows[0]
        return Post(row['id'], row['title'], row['content'], row['views'], row['user_id'])
    
    def create(self, post_instance):
        self._connection.execute('INSERT INTO posts (title, content, views, user_id) VALUES (%s, %s, %s, %s)', [post_instance.title, post_instance.content, post_instance.views, post_instance.user_id])

    def delete(self, post_id):
        self._connection.execute('DELETE FROM posts WHERE id = %s', [post_id])


    # id SERIAL PRIMARY KEY,
    # title TEXT,
    # content TEXT,
    # views INT,
    # user_id INT REFERENCES user_accounts(id)
    # on delete cascade