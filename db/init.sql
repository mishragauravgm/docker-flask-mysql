CREATE DATABASE IF NOT EXISTS users;
USE users;


CREATE TABLE user_data (
  user_name VARCHAR(50),
  user_email VARCHAR(50)
);


INSERT INTO user_data
  (user_name, user_email)
VALUES
  ('Jane Doe', 'email1@example.com'),
  ('John Doe', 'email2@example.com');
