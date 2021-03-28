# flask_user_management

User management system is a web app developed on Flask rest api. It simply register user and get all the user details in a json format.

# Python-Flask Setup
## Prerequisites:
* python 3.6+
* Virtual Environment

## virtual environment:
* pip install virtualenv
* python -m venv folder_name
## activate:
* source folder_name/bin/activate( for linux)
* folder_name\Scripts\activate( for windows)

## Installation and running:
* cd go to project dir
* python -m pip install --upgrade pip
* pip install -r requirements.txt

## Flask code execution:
### for dynamic port run:
* set FLASK_APP= manage.py
* flask run --port=2000 

# How to Run MYSQL Qury:

### Run sql query to mysql terminal:

### login with mysql database:
* mysql -u root -p

## After login run the sql file following sequence:
1. create_database.sql
2. create_user_table.sql
3. create_address_table.sql

## Run all the file using following command:
* source filepath.sql

## How to test request and response

To test the request and response i have used Postman Tool.
