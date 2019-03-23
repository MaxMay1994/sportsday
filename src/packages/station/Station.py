import time
from random import randint
from flask import request
from ...controller.database import DatabaseController
from ..login import Login
from .abstract.AbstractStation import AbstractStation


class Station(AbstractStation):

    def update_points(self):
        db = DatabaseController()
        number_input = []
        students = []
        result = {}
        success = True

        number_input.append(request.form['student_number1'])
        number_input.append(request.form['student_number2'])
        number_input.append(request.form['student_number3'])
        number_input.append(request.form['student_number4'])
        number_input.append(request.form['student_number5'])

        students.append(db.get_student_information({'number': number_input[0]}))
        students.append(db.get_student_information({'number': number_input[1]}))
        students.append(db.get_student_information({'number': number_input[2]}))
        students.append(db.get_student_information({'number': number_input[3]}))
        students.append(db.get_student_information({'number': number_input[4]}))

        for i in range(len(students)):
            if students[i] is not None:
                result[str(number_input[i])] = True
                students[i]['points'] = int(students[i]['points'])
                students[i]['points'] += db.get_current_station()['points']

                if students[i]['ill']:
                    students[i]['ill'] = False

                db.update_points(students[i])
                db.update_student_ill(students[i])
            else:
                if number_input[i]:
                    result[str(number_input[i])] = False
                    success = False

        if not success:
            return result

    def manage_station(self):
        pass

    def add_station(self):
        db = DatabaseController()
        login = Login()
        auth = {'timestamp': time.time(), 'salt': randint(10, 99), 'pin': ''}

        auth['pin'] = login.hash_password(request.form['pin'], auth['timestamp'], auth['salt'])
        return db.insert_station(request.form, auth)
