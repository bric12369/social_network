from lib.database_connection import *
from lib.user_account_repository import *
from lib.post_repository import *

connection = DatabaseConnection()
print(connection.connect())
print(connection.seed('seeds/social_network.sql'))

user_repo = UserAccountRepository(connection)
post_repo = PostRepository(connection)

users = user_repo.all()
[print(user) for user in users]

print('\n')

posts = post_repo.all()
[print(post) for post in posts]