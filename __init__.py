from flask import Flask, redirect, url_for, session, make_response
from src.controller.login import LoginController
from src.controller import Controller
from src.controller.station import StationController
from src.controller.error import ErrorController


app = Flask(__name__)
# set Secret key
app.secret_key = b'_87fgT%5#8jsd32\n\xec]/'


@app.route('/')
def index():
    obj = Controller()
    return obj.main()


@app.route('/login', methods=['GET', 'POST'])
def login_form():
    if 'role' not in session:
        obj = LoginController()
        return obj.get_login_form()

    return redirect(url_for(session['defaultRoute']))


@app.route('/logout')
def logout():
    obj = LoginController()
    return obj.logout()


@app.route('/station', methods=['GET', 'POST'])
def station():
    if 'role' not in session or session['role'] != 'station':
        return redirect(url_for('login_form'))

    obj = StationController()
    return obj.get_station()


@app.route('/dashboard')
def dashboard():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    return redirect(url_for('manage_station'))


@app.route('/dashboard/station')
def dash_station():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    return redirect(url_for('manage_station'))


@app.route('/dashboard/station/verwalten', methods=['GET', 'POST'])
def manage_station():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    obj = StationController()
    return obj.manage_station()


@app.route('/dashboard/station/erstellen', methods=['GET', 'POST'])
def add_station():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    obj = StationController()
    return obj.add_station()


@app.route('/dashboard/klasse')
def dash_class():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    return redirect(url_for('manage_class'))


@app.route('/dashboard/klasse/verwalten')
def manage_class():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    return 0


@app.route('/dashboard/laufzettel')
def dash_docket():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    return redirect(url_for('generate_docket'))


@app.route('/dashboard/laufzettel/generieren')
def generate_docket():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    return 0

# --------------------------------------------------------------
#
# H T T P  -  E R R O R  H A N D L I N G
#
# --------------------------------------------------------------


@app.errorhandler(400)
def internal_error(error):
    obj = ErrorController()
    return obj.get_error_template(error, 400)


@app.errorhandler(403)
def internal_error(error):
    obj = ErrorController()
    return obj.get_error_template(error, 403)


@app.errorhandler(404)
def not_found(error):
    obj = ErrorController()
    return obj.get_error_template(error, 404)


@app.errorhandler(405)
def internal_error(error):
    obj = ErrorController()
    return obj.get_error_template(error, 405)


@app.errorhandler(406)
def internal_error(error):
    obj = ErrorController()
    return obj.get_error_template(error, 406)


@app.errorhandler(500)
def internal_error(error):
    obj = ErrorController()
    return obj.get_error_template(error, 500)


@app.errorhandler(502)
def internal_error(error):
    obj = ErrorController()
    return obj.get_error_template(error, 502)


@app.errorhandler(503)
def internal_error(error):
    obj = ErrorController()
    return obj.get_error_template(error, 503)


app.run()
