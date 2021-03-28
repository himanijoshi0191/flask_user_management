create table address(address_id int NOT NULL AUTO_INCREMENT Primary key,
                    flat_number varchar(50) not null,
                    address_Line_1 varchar(100),
                    address_Line_2 varchar(100),
                    user_id varchar(30) not null,
                    city VARCHAR(32),
                    state varchar(32) NOT NULL,
                    pin_code int NOT NULL,
                    FOREIGN KEY (user_id)REFERENCES user(email));