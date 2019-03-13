from src.controller.database import DatabaseController
from src.controller import Controller
from src.packages.schoolclass import SchoolClass
from flask import redirect, url_for, render_template, request


class SchoolClassController(Controller):
    def __init__(self):
        pass

    def manage_class(self):
        db = DatabaseController()
        cursor = db.get_classes()

        return render_template('class/class_manage.html', classes=cursor)

    def add_class(self):
        error = False

        if request.method == 'POST':
            schoolclass = SchoolClass()
            success = schoolclass.add_class()

            if success:
                return redirect(url_for('class_manage'))

            error = True

        return render_template('class/class_add.html', error=error)