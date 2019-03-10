from src.controller import Controller
from flask import render_template, request, redirect, url_for, session
from src.packages.login import Login


class LoginController(Controller):

    def __init__(self):
        self.superusers = []
        self.stations = []

    def get_login_form(self):
        response = False

        if request.method == 'POST':
            login = Login()
            information = login.validate_login_request()

            if information is not None:
                login.login(information)
                return redirect(url_for(session['defaultRoute']))
            response = True

        return render_template('login/login.html', fehler=response)

    def logout(self):
        login = Login()
        login.logout()

        return redirect(url_for('login_form'))
