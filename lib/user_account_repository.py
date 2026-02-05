from lib.user_account import *
from lib.post import *

class UserAccountRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM user_accounts')
        user_accounts = []
        for row in rows:
            user_account = UserAccount(row['id'], row['email'], row['username'])
            user_accounts.append(user_account)
        return user_accounts
    
    def find_with_posts(self, user_id):
        rows = self._connection.execute('SELECT user_id, email, username, title, content, views, posts.id AS post_id FROM user_accounts JOIN posts ON user_accounts.id = posts.user_id WHERE posts.user_id = %s', [user_id])
        posts = []
        for row in rows:
            post = Post(row['post_id'], row['title'], row['content'], row['views'], row['user_id'])
            posts.append(post)
        user_with_posts = UserAccount(rows[0]['user_id'], rows[0]['email'], rows[0]['username'], posts)
        return user_with_posts