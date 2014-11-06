#create our database to store Facebook Data
CREATE DATABASE facebook_data;
 
#create our table to store the data
USE facebook_data;
CREATE TABLE page_info(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    fb_id BIGINT UNSIGNED,
    likes BIGINT UNSIGNED,
    talking_about BIGINT UNSIGNED,
    username VARCHAR(40),
    time_collected datetime NOT NULL DEFAULT now()
);