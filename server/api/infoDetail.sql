DROP TABLE IF EXISTS InfoDetail CASCADE;

CREATE TABLE InfoDetail (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    uid VARCHAR(255) NOT NULL,
    mobileNum VARCHAR(255) NOT NULL
);

INSERT INTO InfoDetail (name, email, uid, mobileNum) VALUES ('Kush', 'ka8540@g.rit.edu', '387005003', '+15859575220');
