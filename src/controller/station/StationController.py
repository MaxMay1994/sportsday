from src.controller import Controller
from src.controller.login import LoginController
from src.controller.datenbank import DatenbankController
from src.packages.station import Station
from flask import redirect, url_for, render_template, request
from random import randint
import time


class StationController(Controller):
    def __init__(self):
        pass

    def get_station(self):
        db = DatenbankController()

        if request.method == 'POST':
            station = Station()

            student = db.get_student_information({'number': request.form['student']})
            student['points'] = int(student['points'])
            student['points'] += db.get_station_information()['points']
            db.update_points(student)

        station_information = db.get_station_information()

        return render_template('station/station.html', station=station_information)

    def manage_station(self):
        db = DatenbankController()
        cursor = db.get_stations()

        return render_template('station/station_manage.html', stationen=cursor)

    def add_station(self):
        error = False
        db = DatenbankController()

        if request.method == 'POST':
            login = LoginController()
            auth = {'timestamp': time.time(), 'salt': randint(10, 99), 'pin': ''}

            auth['pin'] = login.hash_password(request.form['pin'], auth['timestamp'], auth['salt'])
            success = db.insert_station(request.form, auth)

            if success:
                return redirect(url_for('manage_station'))

            error = True

        return render_template('station/station_add.html', error=error)
