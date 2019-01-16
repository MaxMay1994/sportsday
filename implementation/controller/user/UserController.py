from implementation.controller import Controller
from flask import session, redirect, url_for, render_template, escape


class UserController(Controller):
    def __init__(self):
        pass

    def dashboard(self):
        if 'username' in session and 'role' in session:
            return render_template(session['role'] + '/' + session['role'] + '.html', user=escape(session['username']))
        else:
            return redirect(url_for('login_form'))
