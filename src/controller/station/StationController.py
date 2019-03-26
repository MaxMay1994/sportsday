from .. import Controller
from ..database import DatabaseController
from ...packages.station import Station
from flask import redirect, url_for, render_template, request


class StationController(Controller):
    def get_station(self):
        db = DatabaseController()
        station_information = db.get_current_station()

        if request.method == 'POST':
            station = Station()
            students = station.update_points()

            if students is None:
                return render_template('station/station.html', station=station_information, success='True')

            # make pretty later
            ok = []
            fail = []
            for i in range(len(students)):
                if list(students.values())[i]:
                    ok.append(list(students.keys())[i])
                else:
                    fail.append(list(students.keys())[i])

            return render_template('station/station.html', station=station_information, success='False', fail=fail, ok=ok)

        return render_template('station/station.html', station=station_information)

    def manage_station(self):
        success = None
        db = DatabaseController()
        cursor = db.get_stations()

        if request.method == 'POST':
            station = Station()
            success = station.manage_station()

        return render_template('station/station_manage.html', stationen=cursor, success=success)

    def add_station(self):
        error = False

        if request.method == 'POST':
            station = Station()
            success = station.add_station()

            if success:
                return redirect(url_for('manage_station'))

            error = True

        return render_template('station/station_add.html', error=error)
