from lib.post import *

def test_init_with_atrributes():
    post = Post(1, 'Wednesday', 'Today is Wednesday', 3, 1)
    assert post.id == 1
    assert post.title == 'Wednesday'
    assert post.content == 'Today is Wednesday'
    assert post.views == 3
    assert post.user_id == 1

def test_instances_with_same_attributes_are_equal():
    post1 = Post(1, 'Wednesday', 'Today is Wednesday', 3, 1)
    post2 = Post(1, 'Wednesday', 'Today is Wednesday', 3, 1)
    assert post1 == post2

def test_format():
    post = Post(1, 'Wednesday', 'Today is Wednesday', 3, 1)
    assert str(post) == 'Post(1, Wednesday, Today is Wednesday, 3, 1)'