from src.controller import Controller
from flask import render_template


class ErrorController(Controller):
    def __init__(self):
        pass

    @staticmethod
    def get_error_template(error, error_code):
        return render_template('error/error.html', error_code=error_code, error=error), error_code
