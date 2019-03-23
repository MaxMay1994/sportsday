from src.controller.database import DatabaseController
from src.controller import Controller
from src.packages.schoolclass import SchoolClass
from flask import redirect, url_for, render_template, request
from src.controller.student.StudentController import StudentController


class SchoolClassController(Controller):
    def __init__(self):
        pass

    def manage_class(self):
        db = DatabaseController()
        cursor = db.get_classes()

        schoolclass = SchoolClass()
        success = schoolclass.manage_class()

        return render_template('class/class_manage.html', classes=cursor, success=success)

    def add_class(self):
        error = False

        if request.method == 'POST':
            schoolclass = SchoolClass()
            student_controller = StudentController()
            success = schoolclass.add_class()
            # start move into if success
            student_controller.add_students(request.form['classname'], request.form['amountStudents'])
            # end move into if success
            if success:

                return redirect(url_for('class_manage'))

            error = True

        return render_template('class/class_add.html', error=error)