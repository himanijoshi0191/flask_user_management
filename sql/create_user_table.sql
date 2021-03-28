create table user(user_id int NOT NULL AUTO_INCREMENT Primary key,
                    name varchar(50) not null,
                    email varchar(30) NOT NULL UNIQUE,
                    password VARCHAR(32),
                    profile_picture MEDIUMBLOB,
                    mobile varchar(50) NOT NULL UNIQUE);