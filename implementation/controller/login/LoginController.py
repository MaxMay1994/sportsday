from implementation.controller import Controller
import hashlib
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

            self.superusers = db.get_login_information('superUser')
            self.stations = db.get_login_information('station')

            return self.validate_login()

        return render_template('login/login.html', fehler=False)

    def logout(self):
        session.pop('username', None)
        return redirect(url_for('login_form'))

    def validate_login(self):
        for account in self.superusers:
            if request.form['login-username'] == account['username'] and self.hash_password(request.form['login-password'], account['timestamp'], account['salt']) == account['password']:
                session['username'] = request.form['login-username']
                session['role'] = 'superUser'
                return redirect(url_for('dashboard'))

        for account in self.stations:
            if request.form['login-username'] == account['stationname'] and self.hash_password(request.form['login-password'], account['timestamp'], account['salt']) == account['pin']:
                session['username'] = request.form['login-username']
                session['role'] = 'station'
                return redirect(url_for('dashboard'))

        return render_template('login/login.html', fehler=True)

    def hash_password(self, password, timestamp, salt):
        password_hash = hashlib.sha256(password.encode('utf-8'))
        timestamp_hash = hashlib.sha256(str(timestamp).encode('utf-8'))
        salt_hash = hashlib.sha256(str(salt).encode('utf-8'))

        endhash = hashlib.sha256(password_hash.hexdigest().encode('utf-8') + timestamp_hash.hexdigest().encode(
            'utf-8') + salt_hash.hexdigest().encode('utf-8'))
        return endhash.hexdigest()
