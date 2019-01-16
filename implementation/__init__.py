from flask import Flask, redirect, url_for
from implementation.controller.login import LoginController
from implementation.controller import Controller
from implementation.controller.user import UserController
from implementation.controller.station import StationController
from implementation.controller.datenbank import DatenbankController
from implementation.controller.error import ErrorController


app = Flask(__name__)
# set Secret key
app.secret_key = b'_87fgT%5#8jsd32\n\xec]/'


@app.route('/')
def index():
    obj = Controller()
    return obj.main()


@app.route('/login', methods=['GET', 'POST'])
def login_form():
    obj = LoginController()
    return obj.get_login_form()


@app.route('/logout')
def logout():
    obj = LoginController()
    return obj.logout()


@app.route('/station', methods=['GET', 'POST'])
def station():
    obj = StationController()
    return obj.get_station()


@app.route('/dashboard')
def dashboard():
    return 0


@app.route('/dashboard/station')
def dash_station():
    return redirect(url_for('/dashboard/station/verwalten'))


@app.route('/dashboard/station/verwalten')
def manage_station():
    obj = StationController()
    return obj.manage_station()


@app.route('/dashboard/klasse')
def dash_class():
    return redirect(url_for('/dashboard/klasse/verwalten'))


@app.route('/dashboard/klasse/verwalten')
def manage_class():
    return 0


@app.route('/dashboard/laufzettel')
def dash_slip():
    return redirect(url_for('/dashboard/laufzettel/generieren'))


@app.route('/dashboard/laufzettel/generieren')
def generate_slip():
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
