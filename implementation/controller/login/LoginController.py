from implementation.controller import Controller
import json
from implementation.controller.datenbank import DatenbankController
from flask import render_template, request, session, redirect, url_for


class LoginController(Controller):

    def __init__(self):
        self.superusers = []
        self.stations = []

    def get_login_form(self):
        if 'username' in session:
            return redirect(url_for('dashboard'))

        if request.method == 'POST':
            db = DatenbankController()

            self.superusers = db.get_login_information('SuperUser')
            self.stations = db.get_login_information('Station')

            return self.validate_login()

        return render_template('login/login.html', fehler=False)

    def logout(self):
        session.pop('username', None)
        return redirect(url_for('login_form'))

    def validate_login(self):
        for account in self.superusers:
            if request.form['login-username'] == account['Username'] and request.form['login-password'] == account['Passwort']:
                session['username'] = request.form['login-username']
                session['role'] = 'superUser'
                return redirect(url_for('dashboard'))

        for account in self.stations:
            if request.form['login-username'] == account['Stationname'] and int(request.form['login-password']) == account['PIN']:
                session['username'] = request.form['login-username']
                session['role'] = 'station'
                return redirect(url_for('dashboard'))

        return render_template('login/login.html', fehler=True)
