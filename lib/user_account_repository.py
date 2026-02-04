from lib.user_account import *

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