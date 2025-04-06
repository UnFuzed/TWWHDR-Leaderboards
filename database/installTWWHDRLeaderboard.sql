DROP DATABASE IF EXISTS TWWHDR_Leaderboard;

CREATE DATABASE TWWHDR_Leaderboard;

CREATE TYPE user_role AS ENUM ('admin', 'player', 'owner');

CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    display_name VARCHAR(50) NOT NULL,
    hashed_password VARCHAR(100) NOT NULL,
    role user_role NOT NULL
);

CREATE TABLE Weeks (
    week_id SERIAL PRIMARY KEY,
    week_number INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    start_date TIMESTAMPTZ NOT NULL,
    end_date TIMESTAMPTZ NOT NULL
);

CREATE TABLE Records (
    record_id SERIAL PRIMARY KEY,
    points INT NOT NULL DEFAULT 0,
    completion_time TIME NOT NULL,
    vodLink VARCHAR(255),
    comments VARCHAR(255),
    week_id INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (week_id) REFERENCES Weeks(week_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

CREATE INDEX idx_week_id ON Records(week_id);
CREATE INDEX idx_user_id ON Records(user_id);
