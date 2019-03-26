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
                students[i]['points'] += int(db.get_current_station()['points'])

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
        db = DatabaseController()

        if request.method == 'POST':
            button = request.form.copy().popitem()[0]
            delimiter_position = button.find('-')

            # it's kinda weird, because we need the name of the station without -
            # that's why we add to the position of the delimiter +1
            station_name = button[delimiter_position + 1:]

            if button[0:4] == "save":
                success = self.validate_request_data(station_name)
                if success:
                    search_dict = {'stationname': station_name}
                    update_dict = {"$set": {"stationname": request.form['stationname-' + station_name], "points": int(request.form['points-' + station_name]), "area": request.form['area-' + station_name], "description": request.form['description-' + station_name]}}

                    if request.form['pin-'+station_name] != "":
                        db_station = db.get_station_information({'stationname': station_name})
                        pin_hash = Login().hash_password(request.form['pin-'+station_name], db_station['timestamp'], db_station['salt'])

                        update_dict['$set']['pin'] = pin_hash

                    result = db.update_station(search_dict, update_dict)

                    if result is not None:
                        return True

            elif button[0:6] == "delete":
                result = db.delete_station(station_name)

                if result is not None:
                    return True

        return False

    def add_station(self):
        db = DatabaseController()
        login = Login()
        auth = {'timestamp': time.time(), 'salt': randint(10, 99), 'pin': ''}

        if request.form['points'].isdigit():
            auth['pin'] = login.hash_password(request.form['pin'], auth['timestamp'], auth['salt'])
            return db.insert_station(request.form, auth)

        return False

    def validate_request_data(self, station_name):
        if not request.form['points-' + station_name].isdigit():
            return False

        return True
