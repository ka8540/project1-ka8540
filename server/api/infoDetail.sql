DROP TABLE IF EXISTS InfoDetail CASCADE;

CREATE TABLE InfoDetail (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    uid VARCHAR(255) NOT NULL,
    mobileNum VARCHAR(255) NOT NULL
);

INSERT INTO InfoDetail (firstname,lastname, email, uid, mobileNum) VALUES ('Kush','Ahir','ka8540@g.rit.edu', '387005003', '+15859575220');
