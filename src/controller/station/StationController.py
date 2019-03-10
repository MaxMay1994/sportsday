from src.controller import Controller
from src.controller.database import DatabaseController
from src.packages.station import Station
from flask import redirect, url_for, render_template, request


class StationController(Controller):
    def get_station(self):
        db = DatabaseController()
        station_information = db.get_current_station()

        if request.method == 'POST':
            station = Station()
            success = station.update_points()

            return render_template('station/station.html', station=station_information, success=str(success))

        return render_template('station/station.html', station=station_information)

    def manage_station(self):
        db = DatabaseController()
        cursor = db.get_stations()

        return render_template('station/station_manage.html', stationen=cursor)

    def add_station(self):
        error = False

        if request.method == 'POST':
            station = Station()
            success = station.add_station()

            if success:
                return redirect(url_for('manage_station'))

            error = True

        return render_template('station/station_add.html', error=error)
