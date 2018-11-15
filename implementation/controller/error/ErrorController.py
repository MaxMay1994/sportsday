from implementation.controller import Controller
from flask import render_template


class ErrorController(Controller):
    def __init__(self):
        pass

    def get_error_template(self, error, error_code):
        return render_template('error/error.html', error=error), error_code