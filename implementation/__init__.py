from flask import Flask, redirect, render_template
from implementation.controller.login import LoginController
from implementation.controller import Controller
from implementation.controller.user import UserController
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


@app.route('/dashboard')
def dashboard():
    obj = UserController()
    return obj.dashboard()


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

@app.route('/station/<string:station_id>', methods=['GET'])
def station(station_id):
    # get * from Station where id = station_id;
    station_emoji="⚽"
    station_title = "Fußball"
    station_points = "6"
    station_location = "A005"
    station_description = "Das ist ein Text, der Beschreibt was die Station macht. bla bla hsda hasg ohagöa hagiösd"
    return render_template('station/station.html',
                           station_emoji=station_emoji,
                           station_title=station_title,
                           station_points=station_points,
                           station_location=station_location,
                           station_description=station_description)


app.run()
