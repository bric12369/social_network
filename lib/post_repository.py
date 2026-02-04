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