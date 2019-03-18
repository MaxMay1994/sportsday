import time
from random import randint
from flask import request
from ...controller.database import DatabaseController
from ..login import Login
from .abstract.AbstractStation import AbstractStation


class Station(AbstractStation):

    def update_points(self):
        db = DatabaseController()
        student = db.get_student_information({'number': request.form['student']})

        if student is None:
            return False

        student['points'] = int(student['points'])
        student['points'] += db.get_current_station()['points']

        if student['ill']:
            student['ill'] = False

        db.update_points(student)
        db.update_student_ill(student)

        return True

    def manage_station(self):
        pass

    def add_station(self):
        db = DatabaseController()
        login = Login()
        auth = {'timestamp': time.time(), 'salt': randint(10, 99), 'pin': ''}

        auth['pin'] = login.hash_password(request.form['pin'], auth['timestamp'], auth['salt'])
        return db.insert_station(request.form, auth)
