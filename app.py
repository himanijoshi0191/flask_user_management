from flask import Flask, jsonify, request
from config import app, mysql
from flask_mysqldb import MySQLdb
import yaml
import json
import re


@app.route('/', methods=['GET'])
def get_user():
    json_data = []
    try:
        con = mysql_connection()
        # Get all the users from data base
        all_users = con.execute("select * from user")
        if all_users > 0:
            user_details = con.fetchall()
            user = []
            content = {}
            for result in user_details:
                content = {'id': result['user_id'], 'name': result['name'],
                        'email': result['email'], 'mobile': result['mobile']}
                user.append(content)
                content = {}
            return jsonify(user)
    except Exception as e:
        print(e)
    return "sorry No Data found"


@app.route('/ragister', methods=['POST'])
def ragister_user():
    # create connection
    con = mysql_connection()
    if request.method == 'POST':
        # get user data from frontend
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        profile_picture = request.form.get(
            'profile_picture', '')  # 'delhi.jpg'
        mobile = request.form.get('mobile', '')
        # get address data
        flat_number = request.form.get('flat_number', '')
        address_Line_1 = request.form.get('address_Line_1', '')
        address_Line_2 = request.form.get('address_Line_2', '')
        city = request.form.get('city', '')
        state = request.form.get('state', '')
        pin_code = request.form.get('pin_code', '')
        try:
            # validate data
            if name and flat_number:
                Pattern = re.compile("[7-9][0-9]{9}")
                mobile_match = Pattern.match(mobile)
                if mobile_match and len(mobile) == 10:  # number validate
                    count_mob = con.execute(
                        'SELECT email,mobile FROM user where email ="'+email+'" or mobile= "'+mobile+'"')  # validate mobile
                    if count_mob == 0:
                        #  save User data to database
                        con.execute("insert into user(name,email,password,profile_picture,mobile) values (%s, %s,%s,%s,%s)", (
                            name, email, password, profile_picture, mobile))
                        # save Address Data to database
                        con.execute("insert into address(flat_number, address_Line_1, address_Line_2,city,state, pin_code,user_id)\
                        values (%s, %s,%s,%s,%s,%s,%s)", (flat_number, address_Line_1, address_Line_2, city, state, pin_code, email))
                    else:
                        return 'Fields alredy exist in database'
                else:
                    return 'Mobile no is not valid'
            else:
                return "Fields should not be empty"
            mysql.connection.commit()
            close_connection()
        except Exception as e:
            print(e)
            return("Sorry Record not  Added ")
        return "Record Successfully Added"


# MYSQL DATABASE Connection
def mysql_connection():
    try:
        database_connection = mysql.connection.cursor(
            MySQLdb.cursors.DictCursor)
    except Exception as e:
        return e
    return database_connection



# CLOSE MYSQL Connection
def close_connection():
    try:
        con.close()
    except Exception as e:
        return e
