from implementation.controller import Controller
from implementation.controller.datenbank import DatenbankController
from flask import session, redirect, url_for, render_template, request


class StationController(Controller):
    def __init__(self):
        pass

    def get_station(self):
        if 'username' not in session or 'role' not in session:
            return redirect(url_for('login_form'))

        db = DatenbankController()

        if request.method == 'POST':
            student = db.get_student_information({'number': request.form['student']})
            student['points'] = int(student['points'])
            student['points'] += db.get_station_information()['points']
            db.update_points(student)

        station_information = db.get_station_information()

        return render_template('station/station.html', station=station_information)

    def manage_station(self):
        if 'username' not in session or 'role' not in session:
            return redirect(url_for('login_form'))

        db = DatenbankController()

        station_information = db.get_station_information()
        return render_template('station/station_manage.html', stationen=station_information)

    def add_station(self):
        return render_template('station/station_add.html')
