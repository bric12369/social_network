from lib.user_account_repository import *
from lib.user_account import *

def test_lists_all(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = UserAccountRepository(db_connection)
    assert repository.all() == [
        UserAccount(1, 'example@email.com', 'bob_harris'),
        UserAccount(2, 'example2@email.com', 'john_green'),
        UserAccount(3, 'example3@email.com', 'krissie_thorn')
    ]