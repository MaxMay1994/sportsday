
from ..database import DatabaseController
from .. import Controller
from ...packages.student import Student
import random
from flask import request, redirect


class StudentController(Controller):
    def __init__(self):
        pass

    def add_students(self, school_class, amount):
        student = Student()
        db = DatabaseController()
        number_list = []

        for i in range(int(amount)):
            while True:
                student_number = random.randint(10, 99)
                if student_number not in number_list:
                    number_list.append(student_number)
                    break
            class_number = db.get_class_information({'classname': request.form['classname']}).get('number')
            student.add_student(str(class_number) + str(student_number), school_class)

    def set_ill_state(self):
        db = DatabaseController()

        if request.method == 'POST':
            student = db.get_student_information({'number': request.form['number']})

            if student is None:
                return redirect('/dashboard?success=false')

            student_query = {'number': student['number'], 'ill': True}

            success = db.update_student_ill(student_query)

            if success is not None:
                return redirect('/dashboard?success=true')

            return redirect('/dashboard?success=false')
