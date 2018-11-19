from flask import Flask, redirect, render_template
from implementation.controller.login import LoginController
from implementation.controller import Controller
from implementation.controller.user import UserController

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

# @app.errorhandler(404)
# def not_found(error):
#     return render_template('error.html', error=error), 404
#
#
# @app.errorhandler(500)
# def internal_error(error):
#     return render_template('error.html', error=error), 500


@app.route('/logout')
def logout():
    obj = LoginController()
    return obj.logout()


@app.route('/dashboard')
def dashboard():
    obj = UserController()
    return obj.dashboard()


@app.route('/station/<string:station_id>', methods=['GET'])
def station(station_id):
    # get * from Station where id = station_id;
    return render_template('station/station.html',
                           station_image=station_id)


app.run()
