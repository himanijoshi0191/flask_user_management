# Flask APP Configuration file
from flask import Flask
from db_config import Config
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)
# mysql databse connection
app.config.from_object(Config)
mysql = MySQL(app)

