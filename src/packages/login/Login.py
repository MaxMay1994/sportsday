import hashlib
from flask import session, request, url_for
from werkzeug.utils import redirect

from src.controller.datenbank import DatenbankController
from src.packages.login.abstract.AbstractLogin import AbstractLogin


class Login(AbstractLogin):

    def __init__(self):
        super().__init__()

        self.superUsers = []
        self.stations = []

    def get_login_information(self):
        db = DatenbankController()

        self.superUsers = db.get_information('superUser')
        self.stations = db.get_information('station')

    def validate_login_request(self):
        information = None
        self.get_login_information()

        for account in self.superUsers:
            if request.form['login-username'] == account['username'] and self.hash_password(
                    request.form['login-password'], account['timestamp'], account['salt']) == account['password']:
                information = {'role': 'superUser', 'route': 'dashboard', 'redirect': 'manage_station'}

        for account in self.stations:
            if request.form['login-username'] == account['stationname'] and self.hash_password(
                    request.form['login-password'], account['timestamp'], account['salt']) == account['pin']:
                information = {'role': 'station', 'route': 'station', 'redirect': 'station'}

        return information

    def login(self, information):
        session['username'] = request.form['login-username']
        session['role'] = information['role']
        session['defaultRoute'] = information['route']

    def logout(self):
        session.pop('username', None)
        session.pop('role', None)
        session.pop('defaultRoute', None)

    def hash_password(self, password, timestamp, salt):
        password_hash = hashlib.sha256(password.encode('utf-8'))
        timestamp_hash = hashlib.sha256(str(timestamp).encode('utf-8'))
        salt_hash = hashlib.sha256(str(salt).encode('utf-8'))

        endhash = hashlib.sha256(password_hash.hexdigest().encode('utf-8') + timestamp_hash.hexdigest().encode(
            'utf-8') + salt_hash.hexdigest().encode('utf-8'))
        return endhash.hexdigest()
