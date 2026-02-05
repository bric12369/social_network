from lib.database_connection import *
from lib.user_account_repository import *
from lib.post_repository import *

class Application:
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed('seeds/social_network.sql')

    def run(self):
        print('Welcome to the social network! \n')

        choice = input('What would you like to do? \n  1 - List users \n  2 - List posts \n')

        user_repo = UserAccountRepository(self._connection)
        users = user_repo.all()
        post_repo = PostRepository(self._connection)
        posts = post_repo.all()

        if choice == '1':
            [print(user.username) for user in users]
        elif choice == '2':
            [print(f'{post.title}: {post.content}') for post in posts]
        else:
            print('Invalid choice.')

if __name__ == '__main__':
    app = Application()
    app.run()