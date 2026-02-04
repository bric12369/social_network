DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS user_accounts;

CREATE TABLE user_accounts(
    id SERIAL PRIMARY KEY,
    email TEXT,
    username TEXT
);

CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    views INT,
    user_id INT REFERENCES user_accounts(id)
    on delete cascade
);

INSERT INTO user_accounts (email, username)
VALUES('example@email.com', 'bob_harris');

INSERT INTO user_accounts (email, username)
VALUES('example2@email.com', 'john_green');

INSERT INTO user_accounts (email, username)
VALUES('example3@email.com', 'krissie_thorn');

INSERT INTO posts (title, content, views, user_id)
VALUES('WINDY', 'It is windy today.', 3, 1);

INSERT INTO posts (title, content, views, user_id)
VALUES('Football', '2-0 to West Ham!', 5, 2);

INSERT INTO posts (title, content, views, user_id)
VALUES('Gym', 'Just got a new PB on bench!', 7, 3);