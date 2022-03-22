CREATE DATABASE IF NOT EXISTS  test;
USE test ;

CREATE TABLE  users(
    id int NOT NULL AUTO_INCREMENT UNIQUE,
    user_name varchar(50) NOT NULL,
    user_pass varchar(200) NOT NULL,
    user_email varchar(100) NOT NULL UNIQUE,
    PRIMARY KEY(user_name)
);

CREATE TABLE  tokens(
    user_name varchar(50) NOT NULL,
    token varchar(200) NOT NULL,
    refresh_token varchar(200) NOT NULL,
    PRIMARY KEY(user_name),
    FOREIGN KEY(user_name) REFERENCES users(user_name)
);

CREATE TABLE validate(
    new_token varchar(20) NOT NULL UNIQUE,
    user_email varchar(100) NOT NULL UNIQUE, 
    exp_date int NOT  NULL,
    FOREIGN KEY (user_email) REFERENCES users(user_email)
);

