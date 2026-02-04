from lib.user_account import *

def test_init_with_attributes():
    user = UserAccount(1, 'email@email.com', 'username')
    assert user.id == 1
    assert user.email == 'email@email.com'
    assert user.username == 'username'

def test_instances_with_same_attributes_are_equal():
    user1 = UserAccount(1, 'email@email.com', 'username')
    user2 = UserAccount(1, 'email@email.com', 'username')
    assert user1 == user2

def test_format():
    user = UserAccount(1, 'email@email.com', 'username')
    assert str(user) == 'User(1, email@email.com, username)'