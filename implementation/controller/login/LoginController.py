from implementation.controller import Controller
import json
from implementation.controller.datenbank import DatenbankController
from flask import render_template, request, session, redirect, url_for


class LoginController(Controller):

    def __init__(self):
        pass

    def get_login_form(self):
        if 'username' in session:
            return redirect(url_for('dashboard'))

        if request.method == 'POST':
            db = DatenbankController()
            json.loads(db.get_login_information())

            if request.form['login-username'] == 'admin' and request.form['login-password'] == 'admin':
                session['username'] = request.form['login-username']
                return redirect(url_for('dashboard'))
            else:
                return render_template('login.html', fehler=True)

        return render_template('login/login.html', fehler=False)

    def logout(self):
        session.pop('username', None)
        return redirect(url_for('login_form'))
