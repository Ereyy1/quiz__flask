
CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    best_score INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS question (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    true_answer TEXT NOT NULL,
    f_answer1 TEXT NOT NULL,
    f_answer2 TEXT NOT NULL,
    f_answer3 TEXT NOT NULL
);