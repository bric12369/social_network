from lib.post_repository import *
from lib.post import *

def test_lists_all(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    assert repository.all() == [
        Post(1, 'WINDY', 'It is windy today.', 3, 1),
        Post(2, 'Football', '2-0 to West Ham!', 5, 2),
        Post(3, 'Gym', 'Just got a new PB on bench!', 7, 3)
    ]

def test_create_post(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    new_post = Post(None, 'New', 'This is a new post', 5, 1)
    repository.create(new_post)
    assert repository.all() == [
        Post(1, 'WINDY', 'It is windy today.', 3, 1),
        Post(2, 'Football', '2-0 to West Ham!', 5, 2),
        Post(3, 'Gym', 'Just got a new PB on bench!', 7, 3),
        Post(4, 'New', 'This is a new post', 5, 1)
    ]