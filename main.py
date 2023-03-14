from flask import Flask, render_template, redirect, make_response, request, session, abort

from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data.jobs import Jobs
from data.users import User
import datetime


from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/employee.db")
    app.run(host="127.0.0.1", port=8080)
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.address = "module_1"
    user.position = "captain"
    user.speciality = "research engineer"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)


    user = User()
    user.surname = "Rachel"
    user.name = "Sandel"
    user.age = 18
    user.address = "module_2"
    user.position = "student"
    user.speciality = "inf"
    user.email = "ras@ras.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)


    user = User()
    user.surname = "Mike"
    user.name = "Sarvy"
    user.age = 26
    user.address = "module_3"
    user.position = "freelancer"
    user.speciality = "web"
    user.email = "mis@mis.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)


    user = User()
    user.surname = "Oliver"
    user.name = "Samuel"
    user.age = 34
    user.address = "module_4"
    user.position = "police_officer"
    user.speciality = "researcher"
    user.email = "ols@ols.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)


    db_sess.commit()


if __name__ == '__main__':
    main()