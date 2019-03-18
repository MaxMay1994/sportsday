from flask import render_template, url_for, redirect

from .. import Controller
from ..database import DatabaseController


class UserController(Controller):
    def __init__(self):
        pass

    def user_list(self):
        """actually this route is not used"""
        return render_template('error.html', error_code="418", error="I'm a teapot"), 418

    def student_search(self, student_number):
        """"""
        db = DatabaseController()
        student = db.get_student_information({'number': student_number})

        if student is not False and student is not None:
            return redirect(url_for('student_detail', student_id=student_number))

    def student_detail(self, student_id):
        pass
