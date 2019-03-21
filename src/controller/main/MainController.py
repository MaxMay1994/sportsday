from flask import render_template
from .. import Controller


class MainController(Controller):
    def __init__(self):
        pass

    def index(self):
        """This method returns the index site"""
        return render_template('main/index.html')
