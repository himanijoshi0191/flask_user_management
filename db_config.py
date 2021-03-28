# Database configuration file
import yaml

class Config:
    #read mysql crredential from file
    db = yaml.load(open('db.yaml'))

    MYSQL_HOST = db['db_host']
    MYSQL_USER = db['db_username']
    MYSQL_PASSWORD = db['db_password']
    MYSQL_DB = db['db_schema']
    print(db)