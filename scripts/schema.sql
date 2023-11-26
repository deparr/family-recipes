DROP TABLE IF EXISTS authtoken;
DROP TABLE IF EXISTS comment;
DROP TABLE IF EXISTS authtoken;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS recipe;
DROP TABLE IF EXISTS user_group;
DROP TABLE IF EXISTS group_table;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
    username VARCHAR(16) PRIMARY KEY,
    password_hash TEXT NOT NULL,
    password_salt TEXT NOT NULL,
    email TEXT,
    name TEXT
);
CREATE TABLE user_group (
    username VARCHAR(16) NOT NULL,
    group_id INTEGER NOT NULL,
    PRIMARY KEY (username, group_id),
    CONSTRAINT fk_username
        FOREIGN KEY (username) REFERENCES user(username)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (group_id) REFERENCES group_table(id)
);
CREATE TABLE group_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at DATE
);
CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author VARCHAR(16) NOT NULL,
    recipe_id INTEGER NOT NULL,
    group_id INTEGER NOT NULL,
    content VARCHAR(255),
    created_at DATETIME,
    likes INTEGER DEFAULT 0,
    tags TEXT,
    CONSTRAINT fk_author
        FOREIGN KEY (author) REFERENCES user(username)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (recipe_id) REFERENCES recipe(id),
    FOREIGN KEY (group_id) REFERENCES group_table(id)
);
CREATE TABLE recipe (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    ingredients TEXT,
    instructions TEXT,
    difficulty_level INTEGER,
    image BLOB,
    food_type TEXT,
    recipe_source TEXT
);
CREATE TABLE comment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author VARCHAR(16) NOT NULL,
    content TEXT NOT NULL,
    post_id INTEGER NOT NULL,
    created_at DATETIME,
    edited TINY INT,
    CONSTRAINT fk_author
        FOREIGN KEY (author) REFERENCES user(username)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES post(id),
);
CREATE TABLE authtoken (
    username varchar(16) NOT NULL,
    token char(24) NOT NULL,
    expires_at DATETIME NOT NULL,
    PRIMARY KEY (username, token),
    CONSTRAINT fk_username
        FOREIGN KEY (username) REFERENCES user(username)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
