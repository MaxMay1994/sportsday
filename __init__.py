from flask import Flask, redirect, url_for, session, make_response, request, render_template

from .src.controller.ajax import AjaxController
from .src.controller.database import DatabaseController
from .src.controller.login import LoginController
from .src.controller.main.MainController import MainController
from .src.controller.station import StationController
from .src.controller.docket import DocketController
from .src.controller.error import ErrorController
from .src.controller.student.StudentController import StudentController
from .src.controller.user import UserController
from .src.controller.schoolclasses.SchoolClassController import SchoolClassController

app = Flask(__name__)
# set Secret key
app.secret_key = b'_87fgT%5#8jsd32\n\xec]/'


@app.route('/')
def index():
    obj = MainController()
    return obj.index()


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


@app.route('/user')
def user_list():
    obj = UserController()
    return obj.user_list()


@app.route('/user/<int:student_id>')
def student_detail(student_id):
    obj = UserController()
    return obj.student_detail(student_id)


@app.route('/user/search', methods=['POST'])
def user_search():
    if request.method == 'POST':
        obj = UserController()
        return obj.student_search(request.form['student_number'])

    return ErrorController.get_error_template('Method not allowed', 405)


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

    return render_template('main/dashboard.html', success=request.args.get('success'))


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


@app.route('/dashboard/klasse/verwalten', methods=['GET', 'POST'])
def manage_class():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    obj = SchoolClassController()
    return obj.manage_class()


@app.route('/dashboard/klasse/erstellen', methods=['GET', 'POST'])
def add_class():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    obj = SchoolClassController()
    return obj.add_class()


@app.route('/dashboard/laufzettel', methods=['POST'])
def dash_docket():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    return render_template('docket/form.html')


@app.route('/dashboard/laufzettel/generieren', methods=['POST'])
def generate_docket():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    obj = DocketController()
    return obj.generate_docket()


@app.route('/dashboard/schueler/krank', methods=['POST'])
def ill():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    obj = StudentController()
    return obj.set_ill_state()


@app.route('/dashboard/database', methods=['POST'])
def database():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    return render_template('database/database.html')


@app.route('/dashboard/database/loeschen', methods=['POST'])
def delete():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    obj = DatabaseController()
    obj.database_clear()

    return redirect(url_for('database_empty'))


@app.route('/dashboard/database/leer', methods=['GET'])
def database_empty():
    if 'role' not in session or session['role'] != 'superUser':
        return redirect(url_for('login_form'))

    success_message = 'Die Datenbank wurde erfolgreich gelöscht.'
    success_hint = 'Sie können nun neue Klassen und Stationen anlegen.'

    return render_template('base/success_message.html', success_message=success_message, success_hint=success_hint)


@app.route('/ajax/statistics/index/class', methods=['POST'])
def statistics_index_class():
    return AjaxController().top_3_class()


@app.route('/ajax/statistics/index/student', methods=['POST'])
def statistics_index_student():
    return AjaxController().top_3_student()


@app.route('/ajax/statistics/student/class/<int:student_id>', methods=['POST'])
def statistics_student_class(student_id):
    return AjaxController().student_class(student_id)


@app.route('/ajax/statistics/student/global/<int:student_id>', methods=['POST'])
def statistics_student_global(student_id):
    return AjaxController().student_global(student_id)

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
def not_allowed(error):
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


if __name__ == '__main__':
    app.run()
