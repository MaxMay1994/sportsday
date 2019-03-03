import time
from random import randint

from flask import request

from src.controller.datenbank import DatenbankController
from src.packages.login import Login
from src.packages.station.abstract.AbstractStation import AbstractStation


class Station(AbstractStation):

    def update_points(self):
        db = DatenbankController()
        student = db.get_student_information({'number': request.form['student']})

        if student is None:
            return False

        student['points'] = int(student['points'])
        student['points'] += db.get_current_station()['points']
        db.update_points(student)
        return True

    def manage_station(self):
        pass

    def add_station(self):
        db = DatenbankController()
        login = Login()
        auth = {'timestamp': time.time(), 'salt': randint(10, 99), 'pin': ''}

        auth['pin'] = login.hash_password(request.form['pin'], auth['timestamp'], auth['salt'])
        return db.insert_station(request.form, auth)
